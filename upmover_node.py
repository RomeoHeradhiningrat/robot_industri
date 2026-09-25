import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class MoverNode(Node):
    def __init__(self):
        super().__init__('mover_node')
        
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.start_time = time.time()

    def timer_callback(self):
        msg = Twist()
        current_time = time.time()
        elapsed_time = current_time - self.start_time

        if elapsed_time < 2.0:
            msg.linear.x = 0.5   # Kecepatan linear (m/s)
            msg.angular.z = 0.0
            self.get_logger().info('Gerak Maju Kedepan...')
		elif elapsed_time < 7.0:
			msg.linear.x = 0.0
			msg.angular.z = 0.5 # Kecepatan rotasi (rad/s)
			self.get_logger().info('Belok...')
		elif elapsed_time < 12.0:
            msg.linear.x = 0.5   # Kecepatan linear (m/s)
            msg.angular.z = 0.0
            self.get_logger().info('Gerak Maju Kekiri...')
        elif elapsed_time < 14.0:
            msg.linear.x = 0.0
            msg.angular.z = 0.5  # Kecepatan rotasi (rad/s)
            self.get_logger().info('Belok...')
		elif elapsed_time < 16.0:
            msg.linear.x = 0.5   # Kecepatan linear (m/s)
            msg.angular.z = 0.0
            self.get_logger().info('Gerak Maju Kebawah...')
		elif elapsed_time < 21.0:
            msg.linear.x = 0.0
            msg.angular.z = 0.5  # Kecepatan rotasi (rad/s)
            self.get_logger().info('Belok...')
		elif elapsed_time < 26.0:
            msg.linear.x = 0.5   # Kecepatan linear (m/s)
            msg.angular.z = 0.0
            self.get_logger().info('Gerak Maju Kekanan...')
		elif elapsed_time < 31.0:
            msg.linear.x = 0.0
            msg.angular.z = 0.5  # Kecepatan rotasi (rad/s)
            self.get_logger().info('Belok...')
        else:
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            self.get_logger().info('Berhenti.')
            self.publisher_.publish(msg)
            
            self.timer.cancel()
            rclpy.shutdown()
            return

        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = MoverNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        if rclpy.ok():
            node.destroy_node()
            rclpy.shutdown()

if __name__ == '__main__':
    main()
