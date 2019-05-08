import urllib.request
import json
import turtle
import time


def main():
     def run_turtle(lon, lat):
     
         # Turtle Power
         screen = turtle.Screen() # create a screen object
         screen.setup(720, 360) # Set the resolution
         screen.setworldcoordinates(-180,-90,180,90)
         screen.bgpic('iss_map.gif')
         screen.register_shape('spriteiss.gif')
         iss = turtle.Turtle()
         iss.shape('spriteiss.gif')
         iss.setheading(90)
         iss.penup()
         iss.goto(lon, lat)

         return iss
     
     def return_iss():
        ##Trace the ISS ~ earth-orbital space station
        eoss = 'http://api.open-notify.org/iss-now.json'
     
        ## Call the webservice
        trackiss = urllib.request.urlopen(eoss)
       
        ## put into file object
        ztrack = trackiss.read()
     
        ## json 2 python data structure
        result = json.loads(ztrack.decode('utf-8'))
        return result

     def pin_location(yellat, yellon):
        mylocation = turtle.Turtle()
        mylocation.penup()
        mylocation.color('yellow')
        mylocation.goto(yellat, yellon)
        mylocation.dot(5)
        mylocation.hideturtle()
        return yellowlat, yellowlon, mylocation

     
     def pass_overlay(x):

        passiss = 'http://api.open-notify.org/iss-pass.json'
        passiss = passiss + '?lat=' + str(x[0]) + '&lon=' + str(x[1])
        response = urllib.request.urlopen(passiss)
        result = json.loads(response.read().decode('utf-8'))
     
     #print(result)
     

        over = result['response'][1]['risetime']
        style = ('Arial', 6, 'bold')
        x[2].write(time.ctime(over), font=style)
     
     results = return_iss()
     ## display our pythonic data
     print("\n\nConverted python data")
     print(results)
     input('\nISS data retrieved and converted. Press any key to continue')
     
     location = results['iss_position']
     lat = location['latitude']
     lon = location['longitude']
     print('\nLatitude: ', lat)
     print('\nLongitude: ', lon)
     
     
    
     
   
     lon = round(float(lon))
     lat = round(float(lat))
     yellowlat = round(float(input('Enter your latitude: ' )))
     yellowlon = round(float(input('Enter your longitude: ')))

     x = pin_location(yellowlat, yellowlon)
     pass_overlay(x)
     iss = run_turtle(lon, lat) 
     
     timer = 20
     while (timer != 0):
        return_iss()
        iss.goto(lon, lat)
        timer -= 1
        time.sleep(5)

     turtle.mainloop()
main()
