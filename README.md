# 20211159 Nguyen Thao Nhi - Project 1 Explaination

# 1. A clock

In a traditional analog clock, the second, minute, and hour hands rotate at different rates. The relationships between their rotations are as follows:

The second hand completes a full rotation every 60 seconds.

The minute hand completes a full rotation every 60 minutes (1 hour).

The hour hand completes a full rotation every 12 hours.

Based on this information, if the second hand completes a full rotation (360 degrees), the minute hand would have moved 1/60th of a rotation (6 degrees) and the hour hand would have moved 1/720th of a rotation (0.5 degrees).

However, it would take much time to minute needle to finish a round. Therefore I just mimiced the speed, not to follow the real movement of needles. That's why the needles might not run enough rounds as in the reality.


# 2. A solor system
 
Base on code from clock.py, we can make planets base on the same principle.

- The sun is the center of the whole system
- The Earth and Mars rotates around the sun
- The moon is rotating around the Earth
- The Mars has 2 moons. One of them also has a moon. Each moon rotate in a orbit which has the same center as the host planet.
 

# 3. A robot arm system
 
## Step:

1. Change keyboard function, use Arrow keys to control the three joints and space for gripper on/off action
2. Add three arms and make them rotatable.
3. Draw a gripper and make it on/off action.

    3.1. Gripper have 2 part: Up and down, each part created by 2 rectangles.

    3.2. On each gripper part, the angle of first and second rectangle is fixed.

    3.3. Angle of upper and lower part are controlled by keyboard.

## Control:

1. Use arrow keys:
    - Up and Down: control the angle.
    - Left and Right: change the arm part.
2. Use space key:
    - Press once: gripper will close or open directly.
    - Press more than one: gripper change state every time you press the space key.

  # 4. My own creation: A pendulum clock

  1. Draw clock face
  2. Draw the pendulum
  3. Use the matrix to make the pendulum swing in the defined range
