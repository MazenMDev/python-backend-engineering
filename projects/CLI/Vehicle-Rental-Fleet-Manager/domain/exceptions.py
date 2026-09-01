class VehicleError(Exception):
    pass


class VehicleNotFound(VehicleError):
    pass


class InvalidInput(VehicleError):
    pass


class VehicleUnavailable(VehicleError):
    pass


class ActionFailure(VehicleError):
    pass
