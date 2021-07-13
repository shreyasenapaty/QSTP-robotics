"""Week I Assignment
Simulate the trajectory of a robot approximated using a unicycle model given the
following start states, dt, velocity commands and timesteps
State = (x, y, theta);
Velocity = (v, w) 
1. Start=(0, 0, 0); dt=0.1; vel=(1, 0.5); timesteps: 25
2. Start=(0, 0, 1.57); dt=0.2; vel=(0.5, 1); timesteps: 10
3. Start(0, 0, 0.77); dt=0.05; vel=(5, 4); timestep: 50
Upload the completed python file and the figures of the three sub parts in classroom
"""
import numpy as np
import matplotlib.pyplot as plt

class Unicycle:
    def __init__(self, x: float, y: float, theta: float, dt: float):
        self.x = x
        self.y = y
        self.theta = theta
        self.dt = dt

        # Store the points of the trajectory to plot
        self.x_points = [self.x]
        self.y_points = [self.y]

    def step(self, v: float, w: float, n: int):
        """
        Write the Kinematics model here
        Expectation:
            1. Given v, w and the current state self.x, self.y, self.theta
                and control commands (v, w) for n timesteps, i.e. n * dt seconds,
                return the final pose (x, y, theta) after this time.
            2. Append all intermediate points into the self.x_points, self.y_points list
                for plotting the trajectory.
        Args:
            v (float): linear velocity
            w (float): angular velocity
            n (int)  : timesteps
        Return:
            x, y, theta (float): final pose 
        """
        for i in range(0,n): # range provides necessary constraint as no of increments i.e no of times loop runs is equal to timesteps
            t=i*self.dt #new time after increment
            theta=((self.theta) + (w*t)) #angle (theta) after the time dt has passed
            x=((v/w)*np.sin(theta))-((v/w)*np.sin(self.theta)) # dot x= vcos(theta +wt) therfore integrating w.r.t to dt form 0 to t this equation is obtained
            y=-(v/w)*np.cos(theta)+((v/w)*np.cos(self.theta))  # similar to how x coordinate was found
            self.x_points.append(x) #to add coordinates to list
            self.y_points.append(y) 

        return x, y, theta

    def plot(self, v: float, w: float):
        """Function that plots the intermeditate trajectory of the Robot"""
        plt.title(f"Unicycle Model: {v}, {w}")
        plt.xlabel("X-Coordinates")
        plt.ylabel("Y-Coordinates")
        plt.plot(self.x_points, self.y_points, color="red", alpha=0.75)
        plt.grid()

        # If you want to view the plot uncomment plt.show() and comment out plt.savefig()
        plt.show()
        # If you want to save the file, uncomment plt.savefig() and comment out plt.show()
        # plt.savefig(f"Unicycle_{v}_{w}.png")

if __name__ == "__main__":    
    v1=Unicycle(0,0,0,0.1)
    v1.step(1,0.5,25)
    v1.plot(1,0.5)
    v2=Unicycle(0,0,1.57,0.2)
    v2.step(0.5,1,10)
    v2.plot(0.5,1)
    v3=Unicycle(0,0,0.77,0.05)
    v3.step(5,4,50)
    v3.plot(5,4)
    print("Unicycle Model Assignment")

    # make an object of the robot and plot various trajectories