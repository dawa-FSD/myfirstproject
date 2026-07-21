class SMSAlert:
    def update(self, event):
        print(f"[SMS] {event}")
class AuditLog:
    def update(self, event):
        print(f"[LOG] {event}")