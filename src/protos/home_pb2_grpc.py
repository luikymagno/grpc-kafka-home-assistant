# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import home_pb2 as home__pb2


class LampServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SetLamp = channel.unary_unary(
                '/LampService/SetLamp',
                request_serializer=home__pb2.Lamp.SerializeToString,
                response_deserializer=home__pb2.Status.FromString,
                )
        self.GetLamp = channel.unary_unary(
                '/LampService/GetLamp',
                request_serializer=home__pb2.Empty.SerializeToString,
                response_deserializer=home__pb2.Lamp.FromString,
                )


class LampServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SetLamp(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLamp(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LampServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SetLamp': grpc.unary_unary_rpc_method_handler(
                    servicer.SetLamp,
                    request_deserializer=home__pb2.Lamp.FromString,
                    response_serializer=home__pb2.Status.SerializeToString,
            ),
            'GetLamp': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLamp,
                    request_deserializer=home__pb2.Empty.FromString,
                    response_serializer=home__pb2.Lamp.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'LampService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class LampService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SetLamp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/LampService/SetLamp',
            home__pb2.Lamp.SerializeToString,
            home__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLamp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/LampService/GetLamp',
            home__pb2.Empty.SerializeToString,
            home__pb2.Lamp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class AirConditionerServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SetAirConditioner = channel.unary_unary(
                '/AirConditionerService/SetAirConditioner',
                request_serializer=home__pb2.AirConditioner.SerializeToString,
                response_deserializer=home__pb2.Status.FromString,
                )
        self.GetAirConditioner = channel.unary_unary(
                '/AirConditionerService/GetAirConditioner',
                request_serializer=home__pb2.Empty.SerializeToString,
                response_deserializer=home__pb2.AirConditioner.FromString,
                )


class AirConditionerServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SetAirConditioner(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAirConditioner(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AirConditionerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SetAirConditioner': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAirConditioner,
                    request_deserializer=home__pb2.AirConditioner.FromString,
                    response_serializer=home__pb2.Status.SerializeToString,
            ),
            'GetAirConditioner': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAirConditioner,
                    request_deserializer=home__pb2.Empty.FromString,
                    response_serializer=home__pb2.AirConditioner.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'AirConditionerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AirConditionerService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SetAirConditioner(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AirConditionerService/SetAirConditioner',
            home__pb2.AirConditioner.SerializeToString,
            home__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAirConditioner(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AirConditionerService/GetAirConditioner',
            home__pb2.Empty.SerializeToString,
            home__pb2.AirConditioner.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class AudioSystemServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SetAudioSystem = channel.unary_unary(
                '/AudioSystemService/SetAudioSystem',
                request_serializer=home__pb2.AudioSystem.SerializeToString,
                response_deserializer=home__pb2.Status.FromString,
                )
        self.GetAudioSystem = channel.unary_unary(
                '/AudioSystemService/GetAudioSystem',
                request_serializer=home__pb2.Empty.SerializeToString,
                response_deserializer=home__pb2.AudioSystem.FromString,
                )


class AudioSystemServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SetAudioSystem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAudioSystem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AudioSystemServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SetAudioSystem': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAudioSystem,
                    request_deserializer=home__pb2.AudioSystem.FromString,
                    response_serializer=home__pb2.Status.SerializeToString,
            ),
            'GetAudioSystem': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAudioSystem,
                    request_deserializer=home__pb2.Empty.FromString,
                    response_serializer=home__pb2.AudioSystem.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'AudioSystemService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AudioSystemService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SetAudioSystem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AudioSystemService/SetAudioSystem',
            home__pb2.AudioSystem.SerializeToString,
            home__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAudioSystem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AudioSystemService/GetAudioSystem',
            home__pb2.Empty.SerializeToString,
            home__pb2.AudioSystem.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
