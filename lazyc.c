#include<stdio.h>
#include <stdlib.h>
#include <string.h>
#include "ornek.h"

//extern int x=32;



int main(){


//tek satırlık yorum
/* çok satırlı yorum

*/

//standart yazı yazdırma komutu
 /*
printf("deneme:\n"); // \n anlamı booşluk ekleme komutudur
return 0;

 return eklenmesinin sebebi main fonksiyonunu  sonlandırmasıdır 
siz eklemeseniz bile derleyeci otomatik olarak ekler
*/



//temel veri tipleri 
 /*
int sayi=1;
float ondalik=1.2123;
double ondalikdoub=12.123213;
char ch = 'A';
char string[20] =" bu bir kelimedir";
int octal=20;
int hexadecimal=20;
printf("%d,%f,%lf,%c,%s,%o,%x \n",sayi,ondalik,ondalikdoub,ch,string,octal,hexadecimal); 
return 0;

printf("%d,%f,%lf,%c,%s,%o,%x \n" kodun bu parçasında belirteçler (%d ,%x) kullanarak değişkenlerin hangi veritipine ait olduğunu belirttik.Zaten değişken sırasına göre belirteç kullandım.

*/

//sizeof fonksiyonu
 /*
printf("%d \n",sizeof(int));
printf("%d \n",sizeof(float));
printf("%d \n",sizeof(double));  
printf("%d \n",sizeof(char));    
return 0;
veri tiplerinin kaç byte yer kapladığını bu şekilde görebilirsiniz.
*/


//extern kullanarak  dışardan değişken eklenebilir
/*
printf("%d \n",x);    
return 0;
*/


//variables
/*
int a,b;
int c;
a=10;
b=20;
c=a+b;
float f;
printf("%d \n",c);
f=70.0/30.0;
printf("%f \n",f);
return 0;
*/


//array(diziler)
/*

int sirano[10];
printf("%d \n",sirano[1]);
//çıktınız 0 olacaktır

int sirano[10];
sirano[1]=260;// 1.nesneyi 1 olarak tanımladık (aslında 2 ancak bilgisayarlarda 0 1 2 şeklinde sayım yapılır
printf("%d \n",sirano[1]);


int sirano[11]={0,1,2,3,4,5,6,7,8,9,10};
int k;
int sizefinder=sizeof(sirano)/sizeof(sirano[0]);//arrayin uzunluğunu belirten fonksiyon
for(k=0;k<sizefind;k++){
printf("%d \n",sirano[k]);
}

*/

//iki boyutlu diziler
/*
int a[2][3] = {{1, 3, 0}, {-1, 5, 9}};
int sum=0;
for(int k =0;k<2;k++){
for(int j =0;j<2;j++){
sum+=a[k][j];
}
}
printf("sum %d \n",sum);
*/


//structures
/*
struct student{
int age;
char grade[40];
char name[40];
};
struct student s1={19,"graduate","name"};
printf(" %s ,%s,%d \n",s1.name,s1.grade,s1.age);
bu yapılar istenilen yapıları oluşturmaya yarar.

//typedef kullanarak bir struct yapısını istediğimiz kadar kullanabiliriz
coordinate coordinates[3]={{2,6,7},{5,7,8},{6,8,9}};
int k,volume ,volume1,volume2;
for(k=0;k<3;k++)
{
volume=coordinates[k].x;
volume1=coordinates[k].y;
volume2=coordinates[k].z;
printf("%d %d %d \n",volume,volume1,volume2);

}

//union 
union val test;
test.intval=123;
test.fl_num=123,87;
strcpy(test.str,"hello");
printf("%d,%f,%s\n",test.intval,test.fl_num,test.str);
//çıktısı ise 1819043176,1143141483620823940762435584.000000, hello 



union val test;
test.intval=123;
printf("%d \n",test.intval);
test.fl_num=123.87;
printf("%f \n",test.fl_num);
strcpy(test.str,"hello");
printf("%s\n",test.str);
çıktısı
123 
123.870003 
hello


return 0;





*/

union val test;
test.intval=123;
printf("%d \n",test.intval);
test.fl_num=123.87;
printf("%f \n",test.fl_num);
strcpy(test.str,"hello");
printf("%s\n",test.str);


return 0;




}



