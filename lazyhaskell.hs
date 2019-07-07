main :: IO() 
-- |main içerisine io input output için library ekledik

add :: Integer -> Integer -> Integer   --function declaration 
add x y =  x + y                       --function definition 

fType :: Int -> Int -> Int 
fType x y = x*x + y*y 

main = do 
-- |değişken atama
   let var1 = 2  
   let var2 = 3 
-- |putStrLn  veya print(+değişken) ile yazı yazdırabiliyouz
   putStrLn "The Multiplication of the Two Numbers is:" 
   print(var1 * var2)
-- |tipler derleme zamanı kullanılan ifadelerdir Int,Integer,Float,Double,Char 
-- |not int ile integer  arasında fark uzunluktadır ancak integer sınırsızdır
-- |EQ yani eşitlikler için  "==" or "/="
   print(add 2 5) 
   print (fType 2 3)
-- | + - * / rem mod quet kullanılabilir
   putStrLn "getout"
   print [1..2]
-- |koşul yönetimi.
   let var = 23 
   if var == 0 
      then putStrLn "Number is zero" 
   else if var `rem` 2 == 0 
      then putStrLn "Number is Even" 
   else putStrLn "Number is Odd"

--haskell kaynakları
--https://www.tutorialspoint.com/haskell/haskell_functions.htm
--https://lotz84.github.io/haskellbyexample/ex/range

