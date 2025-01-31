class SagaStep:
    def __init__(self, action, compensation):
        """
        :param action: Function to perform the main task.
        :param compensation: Function to undo the task if needed.
        """
        self.action = action
        self.compensation = compensation

class Saga:
    def __init__(self):
        self.steps = []  # List of SagaStep
        self.completed_steps = []  # Tracks completed steps for rollback
    
    def add_step(self, action, compensation):
        self.steps.append(SagaStep(action, compensation))
    
    def execute(self):
        try:
            for step in self.steps:
                step.action()  # Execute the action
                self.completed_steps.append(step)  # Track completed step
        except Exception as e:
            print(f"Error occurred: {e}. Initiating rollback...")
            self.rollback()  # Roll back completed steps
            raise e
    
    def rollback(self):
        for step in reversed(self.completed_steps):
            try:
                step.compensation()  # Execute the compensation
            except Exception as e:
                print(f"Error during rollback: {e}")

# Example actions and compensations
def deduct_payment():
    print("Payment deducted.")
    # Simulate success or failure
    # raise Exception("Payment failed!")  # Uncomment to simulate failure

def refund_payment():
    print("Payment refunded.")

def reserve_inventory():
    print("Inventory reserved.")
    # Simulate success or failure
    # raise Exception("Inventory reservation failed!")  # Uncomment to simulate failure

def release_inventory():
    print("Inventory released.")

def create_shipment():
    print("Shipment created.")
    # Simulate success or failure
    # raise Exception("Shipment creation failed!")  # Uncomment to simulate failure

def cancel_shipment():
    print("Shipment canceled.")

# Define the saga workflow
saga = Saga()
saga.add_step(deduct_payment, refund_payment)
saga.add_step(reserve_inventory, release_inventory)
saga.add_step(create_shipment, cancel_shipment)

# Execute the saga
try:
    saga.execute()
    print("All steps completed successfully.")
except Exception:
    print("Saga execution failed.")
