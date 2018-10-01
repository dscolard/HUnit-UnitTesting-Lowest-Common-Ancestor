module LcaSpec where

import   LCA
import   Test.Hspec
import   Test.QuickCheck


--Tests
main :: IO ()
main = hspec $ do
  describe "Lowest Common Ancestor Function" $ do

   it "returns 'not found' for 0 9" $ do
      lca_show myTree 0 9 `shouldBe` "LCA(0,9) = not found"

   it "returns 'not found' for 0 5" $ do
      lca_show myTree 0 5 `shouldBe` "LCA(0,5) = not found"

   it "returns 'not found' for 4 5" $ do
      lca_show myTree 4 5 `shouldBe` "LCA(4,5) = 2"

   it "returns 'not found' for 4 6" $ do
      lca_show myTree 4 6 `shouldBe` "LCA(4,6) = 1"

   it "returns 'not found' for 3 4" $ do
      lca_show myTree 3 4 `shouldBe` "LCA(3,4) = 1"

   it "returns 'not found' for 2 4" $ do
      lca_show myTree 2 4 `shouldBe` "LCA(2,4) = 2"

   it "returns 'not found' for 9 10" $ do
      lca_show myTree 9 10 `shouldBe` "LCA(9,10) = 3"