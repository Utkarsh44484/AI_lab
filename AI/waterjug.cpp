#include <bits/stdc++.h>
using namespace std;
// bool check(int juga,int jugb, int goal){
//     if (juga==goal or juga==goal)
//     {
//       return true;
//     }
//     return false;
// }
void print(int juga,int jugb){
    cout<<"\nJug 1 : "<<juga<<"  "<<"Jug 2 : "<<jugb;
}

// void fill(int juga,int jugb,int goal){
//     if (check) return;
//     else if()
// }

void pour_water(int juga, int jugb){
    int max1 =3,max2 =4,goal=2;
    print(juga, jugb);
    if (jugb==goal)  {  
        return;}
    else if (jugb==max2){
            pour_water(0, juga);}
    else if (juga!=0 and jugb==0){
            pour_water(0,juga);}
    else if (juga==goal){
            pour_water(juga,0);}
    else if (juga<max1){
            pour_water(max1, jugb);}
    else if (juga<(max2-jugb)){
            pour_water(0,(juga+jugb));}
    else{
        pour_water(juga-(max2-jugb), (max2-jugb)+jugb);}

}

int main()
{
    int juga,jugb,goal,n;
    cout<<"Enter capacity of Jug 1(smaller capacity)"<< endl;
    cin>>juga;
    cout<<"Enter capacity of Jug 2(greater capacity)"<< endl;
    cin>>jugb;
    // cout<<"Enter jug no. to fill first : ";
    // cin>>n;
    // // print(0,0);
    // if(n==1){
    //     pour_water(juga,0);
    // }
    // else{
    //    pour_water(0,jugb);
    // }
    pour_water(0,0);
  return 0;
}