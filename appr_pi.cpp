/*This code calculates the value of pie up to n decimal digits. By the simple analogous of collision of 2 boxes.
One box is kept at 0 velocity near to a wall and another mass of (10^n) times of the first collides with the first
box. the no of collisions happened by the first box is the approximation to pi. The collision happens on a friction
 less surface*/

//It takes lots of time and works for less than 10 digits
#include<iostream>
using namespace std;

//This class is the property of the box i.e mass velocity and position w.r.t. the wall
class Box{
    public:
    long long int mass;long double velocity,position;
    Box(long long int mass,long double velocity){
        this->mass=mass;
        this->velocity=-velocity;
        this->position=double(mass);
    }
};
//This function finds the velocities after the collision
void coll_velocity(Box &b1,Box &b2){
    long double momentum=b1.mass*b1.velocity+b2.mass*b2.velocity;
    long double vel=b1.velocity-b2.velocity;

    long long int delta=b1.mass+b2.mass;
    b2.velocity=(momentum+b1.mass*vel)/delta;
    b1.velocity=(momentum-b2.mass*vel)/delta;
    }
//This function where the next collision is going to happen
void next_collision(Box &b1,Box &b2,int click){
    long double time_b1_wall=0;//-(b1.position)/b1.velocity;
    long double time_b1_b2 = 0;//(b1.position - b2.position) / (b2.velocity - b1.velocity);
        if (b1.velocity!=0)
        time_b1_wall = -(b1.position) / b1.velocity;
    if (b1.velocity!=b2.velocity)
        time_b1_b2 = (b1.position - b2.position) / (b2.velocity - b1.velocity);
          if (click==1){
            if (time_b1_wall>0){
                b1.position=0;
                b2.position+=b2.velocity*time_b1_wall;}
            else
                b1.position=-1;}
    else if (click==0 and time_b1_b2>0){
        b1.position+=b1.velocity*time_b1_b2;
        b2.position=b1.position;}
    else    return;
    }

//this function counts the collisions by recursion


long long int coll(Box &b1,Box &b2){
    long long int i=0;
    while(b1.velocity<0 or b1.velocity>=b2.velocity){
   // cout<<i<<endl;
       // if (i>=3) break;
        if (b1.position==0){
            b1.velocity = -b1.velocity;
            next_collision(b1, b2, 0);
            i++;}
        else if( b1.position == b2.position){
        //cout<<"ok"<<endl;
            coll_velocity(b1, b2);
           //cout<<"Velocity of b1="<<b1.velocity<<endl;
          // cout<<"Velocity of b2="<<b2.velocity<<endl;
            next_collision(b1, b2, 1);
            //cout<<"pos of b1="<<b1.position<<endl;
           //cout<<"pos of b2="<<b2.position<<endl;
            i++;}
        else
            {cout<<"why??";break;}

   // cout<<"Velocity of b1="<<b1.velocity<<endl;
   // cout<<"comparison of b1-b2="<<b1.velocity-b2.velocity<<endl<<endl;}
    }return i;
}
int main(){
    Box b1=Box(1,0);
    int n=0;
    cout<<"n= ";cin>>n;
    n=n*2;
   long long int b=1;
    for(int i=0;i<n;i++){
     b=b*10;
    }
    cout<<"b="<<b<<endl;
    Box b2=Box(b,10.0);
    b1.position=b2.position;
   // cout<<"Initially"<<endl<<"Velocity of b1="<<b1.velocity<<endl<<"Velocity of b2="<<b2.velocity<<endl<<endl;
   // print("Velocity of )
    cout<<coll(b1,b2);
    //cout<<col;
    return 0;
}

