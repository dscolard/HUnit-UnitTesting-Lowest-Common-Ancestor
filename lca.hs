
-- Lowest Common Ancestor on binary tree.

import Text.Printf

data Tree a = Empty | Node a (Tree a) (Tree a) deriving Show

--Create tree
myTree :: Tree Int
myTree = Node 1 
	    (Node 2 
	        (Node 4 Empty Empty)
	        (Node 5 Empty Empty)
	    )
	    (Node 3 
	        (Node 6 
	            (Node 10 Empty Empty) 
	            (Node 8 Empty Empty)
	        )
	        (Node 7 
	            (Node 9 Empty Empty) 
	            Empty
	        )
	    )

--Solve for common ancestor
lca :: Eq a => Tree a -> a -> a -> Either Bool a
lca Empty _ _ = Left False
lca (Node v tl tr) n1 n2 = 
    let l = lca tl n1 n2
        r = lca tr n1 n2
        onroot = v == n1 || v == n2
    in case (l, r, onroot) of
        (Right a  , _         , _    ) -> Right a
        (_        , Right a   , _    ) -> Right a
        (Left True, Left True , _    ) -> Right v
        (Left True, _         , True ) -> Right v
        (_        , Left True , True ) -> Right v
        (Left True, _         , False) -> Left True
        (_         , Left True, False) -> Left True
        (_         , _        , True ) -> Left True
        _ -> Left False

lca_show :: (Eq a, Show a, PrintfArg a) => Tree a -> a -> a -> String
lca_show t n1 n2 = printf "LCA(%d,%d)=%s" n1 n2 result
    where result = case lca t n1 n2 of
                        Right a -> show a
                        _ -> "not found"

--Test for examples
main = mapM print [
            lca_show myTree 0 9, --Expected: "not found"
            lca_show myTree 0 5, --Expected: "not found"
            lca_show myTree 4 5, --Expected: "2"
            lca_show myTree 4 6, --Expected: "1"
            lca_show myTree 3 4, --Expected: "1"
            lca_show myTree 2 4, --Expected: "2"
            lca_show myTree 9 10]--Expected: "3"








