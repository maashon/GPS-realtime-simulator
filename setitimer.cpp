extern "C" {
#include <stdio.h>
}
extern "C" {
#include <stdlib.h>
}

extern "C" {
#include <sys/time.h>
}

extern "C" {
#include <signal.h>
}

extern "C" {
#include <time.h>
}
extern "C" {
#include <unistd.h>
}

#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;
struct itimerval timer;
int pCount=0;
int carID=-1;
int pointNumber=0;
bool carAvailability=true;

struct coordinate{
  string latitude;
  string longtitude;
  
  };
  
  vector<coordinate> points;
void handlersetitimer(int signalnumber)
{
  pCount++;
  
    string comand="python sendLocation.py "+to_string(carID)+" "+points[pCount].latitude+" "+points[pCount].longtitude;
    if (pCount==pointNumber){
    pCount=0;
    reverse(points.begin(),points.end());
    }
    int n = comand.length();
    char char_command[n + 1];
    strcpy(char_command, comand.c_str());
     system(char_command);
  
}
int main(int argc, char *argv[])
{
  

  //setting the timer
  struct sigaction sigact;
  sigemptyset(&sigact.sa_mask); //no blocked signals only the one, which arrives
  sigact.sa_handler = handlersetitimer;
  sigact.sa_flags = 0;               //no special behaviour
  sigaction(SIGALRM, &sigact, NULL); //an alarm signal is set

  timer.it_interval.tv_sec = 4;   /* it will be repeated after 3 seconds */
  timer.it_interval.tv_usec = 0;  /* usec - microseconds - 10^(-6) seconds */
  timer.it_value.tv_sec = 12;      /* remaining time till expiration */
  timer.it_value.tv_usec = 0;

  setitimer(ITIMER_REAL, &timer, NULL); //result = 0, if it is good
  if (argc<2||argc>2){
    printf("the car id is not entered in a valid format");
    raise(SIGTERM);
    
    }else{
      carID=atoi(argv[1]);
      }
      srand(time(NULL));
      int fileNumber=3;
      int fName=(rand()%fileNumber)+1;
      std::string adress="";
      adress=to_string(fName)+".dat";
      cout<<adress<<" opened."<<endl;
      ifstream MyReadFile(adress);
      string line;
      coordinate c;
      string lat,longt;
      while (getline(MyReadFile, line)) {
        pointNumber++;
        lat=line.substr(0,line.find(" "));
        line.erase(0, line.find(" ") +1);
        longt=line.substr(0, line.length() );
        c.latitude=lat;
        c.longtitude=longt;
        points.emplace_back(c);
        
        
        }
      MyReadFile.close();
      cout<<"Done reading the file data"<<endl;
      //initializing the car
      /*
      string comand="python init.py "+to_string(carID);
      int n = comand.length();
      char char_command[n + 1];
      strcpy(char_command, comand.c_str());
      system(char_command);
      // setting the listener
      cout<<"done initializing the car"<<endl;
      * */
      string comand2="python makeCar.py "+to_string(carID);
      int n2 = comand2.length();
      char char_command2[n2 + 1];
      strcpy(char_command2, comand2.c_str());
      system(char_command2);
      cout<<"Done making the car"<<endl;
      
      string comand3="python listener.py "+to_string(carID);
      int n3 = comand3.length();
      char char_command3[n3 +1];
      strcpy(char_command3, comand3.c_str());
      system(char_command3);
      
      
      
                
  return 0;
}
