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

using namespace std;
struct itimerval timer;
int count=0;
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
  
 
 
  
  
  count++;
  if (count==10){
    raise(SIGTERM);
    }
    //time_t current_time=time(NULL);
    //string sTime=ctime(&current_time);
  //string comand="python sendLocation.py "+to_string(carID)+" "+points[count].latitude+" "+points[count].longtitude+" "+sTime;
    string comand="python sendLocation.py "+to_string(carID)+" "+points[count].latitude+" "+points[count].longtitude;
    int n = comand.length();
    char char_command[n + 1];
    strcpy(char_command, comand.c_str());
     system(char_command);
    //cout << "\033[2J\033[1;1H";
    //cout<<"writing pos "<<count<<"remain "<<pointNumber-count<<endl;
  
  
  
 
}
int main(int argc, char *argv[])
{
  


  struct sigaction sigact;
  sigemptyset(&sigact.sa_mask); //no blocked signals only the one, which arrives
  sigact.sa_handler = handlersetitimer;
  sigact.sa_flags = 0;               //no special behaviour
  sigaction(SIGALRM, &sigact, NULL); //an alarm signal is set

  timer.it_interval.tv_sec = 1;   /* it will be repeated after 3 seconds */
  timer.it_interval.tv_usec = 0;  /* usec - microseconds - 10^(-6) seconds */
  timer.it_value.tv_sec = 1;      /* remaining time till expiration */
  timer.it_value.tv_usec = 0;

  setitimer(ITIMER_REAL, &timer, NULL); //result = 0, if it is good
  if (argc<2||argc>2){
    printf("the car id is not entered in a valid format");
    raise(SIGTERM);
    
    }else{
      carID=atoi(argv[1]);
      }
      std::string adress="";
      adress=to_string(carID)+".dat";
      cout<<adress<<endl;
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
      
                                        
while(1){
  
  
  
  
  }
  return 0;
}
