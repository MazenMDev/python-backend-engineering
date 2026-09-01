from datetime import datetime


class Rental:
    def __init__(self, kind, vehicleID, name, days, timestamp=None, cost=None):
        self.kind = kind
        self.vehicleID = vehicleID
        self.name = name
        self.days = days
        if timestamp is None:
            self.timestamp = datetime.now()
        else:
            self.timestamp = timestamp
        self.cost = cost

    def to_dict(self) -> dict:
        return {
            "kind": self.kind,
            "vehicleID": self.vehicleID,
            "customer_name": self.name,
            "number_days": self.days,
            "timestamp": self.timestamp.isoformat(),
            "cost": self.cost,
        }

    @classmethod
    def from_dict(cls, data) -> "Rental":
        return cls(
            data["kind"],
            data["vehicleID"],
            data["customer_name"],
            data["number_days"],
            datetime.fromisoformat(data["timestamp"]),
            data["cost"],
        )

    def __str__(self) -> str:
        when = self.timestamp.strftime("%Y-%m-%d %H:%M")
        cost_str = f"${self.cost:.2f}" if self.cost is not None else "-"
        return f"{when}  {self.kind:<8} {self.name:<12} {self.days} day(s)  cost: {cost_str}"
