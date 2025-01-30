#mMTC
class mMTC:
    def __init__(self, device_count):
        self.device_count = device_count

    def allocate_resources(self, user):
        print(f"Allocating mMTC resources for {user}. Supported devices: {self.device_count}")
