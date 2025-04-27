# Import the Tello drone control module
from djitellopy import tello
# Import OpenCV for computer vision and video processing
import cv2


def process_tello_video(drone):
    """
    Handles video streaming and recording from the Tello drone,
    plus basic keyboard controls.

    Parameters:
        drone (tello.Tello): The connected Tello drone instance
    """

    # Initialize video frame capture from the drone
    # This creates a continuous frame reader object that gets the latest camera frame
    frame_read = drone.get_frame_read()

    # VideoWriter configuration:
    # 1. fourcc is a 4-character code specifying the video codec (XVID is a good default)
    # 2. The *'XVID' syntax unpacks the string into four separate characters ('X','V','I','D')
    # 3. The parameters are: filename, codec, fps, and frame size
    fourcc = cv2.VideoWriter.fourcc(*'XVID')
    out = cv2.VideoWriter('tello_recording.avi', fourcc, 30.0, (960, 720))

    # Main video processing loop
    while True:
        # Get the current frame from the drone
        frame = frame_read.frame

        # Resize the frame to our desired dimensions
        # Important: Must match the dimensions we specified in VideoWriter!
        frame = cv2.resize(frame, (960, 720))

        # Display the frame in a window
        cv2.imshow("Tello Camera", frame)

        # Write the frame to our video file
        out.write(frame)

        # Wait for keypress with 1ms delay (needed for imshow to work)
        # The 0xFF mask is used to get the last 8 bits (ASCII value) on 64-bit systems
        key = cv2.waitKey(1) & 0xFF

        # Control commands - these demonstrate direct drone control while streaming
        if key == ord('q'):
            break  # Exit the video loop
        elif key == ord('w'):
            drone.move_forward(30)  # Move forward 30cm
        elif key == ord('s'):
            drone.move_back(30)  # Move backward 30cm
        elif key == ord('a'):
            drone.move_left(30)  # Move left 30cm
        elif key == ord('d'):
            drone.move_right(30)  # Move right 30cm
        elif key == ord('u'):
            drone.move_up(30)
        elif key == ord('x'):
            drone.move_down(30)
        elif key == ord('e'):
            drone.rotate_clockwise(30)  # Rotate 30 degrees clockwise

    # Cleanup resources - important to preventw file corruption!
    out.release()  # Close the video file
    cv2.destroyAllWindows()  # Close all OpenCV windows


# Main execution block
try:
    # Initialize Tello drone connection
    drone = tello.Tello()

    # Connect to the drone via WiFi
    # Note: You must be connected to the Tello's WiFi network first!
    drone.connect()

    # Start video streaming
    # This initializes the video feed but doesn't start displaying it yet
    drone.streamon()

    # Takeoff sequence
    drone.takeoff()  # This command makes the drone take off
    # Start video processing and control loop
    process_tello_video(drone)

finally:
    # This block runs even if there's an error above
    # Ensures we don't leave the drone stranded in the air

    # Land the drone safely
    drone.land()

    # Cleanup drone connection
    # This is important to free resources and properly close the connection
    drone.end()