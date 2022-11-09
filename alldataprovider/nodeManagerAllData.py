# MIT License
#
# Copyright (c) 2020-2022 Bosch Rexroth AG
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from ctrlxdatalayer.provider import Provider
from ctrlxdatalayer.variant import Variant

from alldataprovider.providerNodeAllData import ProviderNodeAllData

class NodeManagerAllData:

    def __init__(self, provider: Provider, addressRoot: str):
        self.provider = provider
        self.addressRoot = addressRoot
        self.nodes = []

    def create_static_nodes(self):
        self.create_nodes("static/", False)

    def create_dynamic_nodes(self, ):
        self.create_nodes("dynamic/", True)

    def create_nodes(self, address: str, dynamic: bool):
        addressBranch = self.addressRoot + address

        data = Variant()
        data.set_bool8(True)
        self.create_single_node(addressBranch, "", "bool8",
                                "unit", "description", dynamic, data)

        data = Variant()
        data.set_int8(-127)
        self.create_single_node(addressBranch, "", "int8",
                                "unit", "description", dynamic, data)

        data = Variant()
        data.set_uint8(255)
        self.create_single_node(addressBranch, "", "uint8",
                                "unit", "description", dynamic, data)

        data = Variant()
        data.set_int16(-32767)
        self.create_single_node(addressBranch, "", "int16",
                                "unit", "description", dynamic, data)

        data = Variant()
        data.set_uint16(65535)
        self.create_single_node(addressBranch, "", "uint16",
                                "unit", "description", dynamic, data)

        data = Variant()
        data.set_int32(0x80000001)
        self.create_single_node(addressBranch, "", "int32",
                                "unit", "description", dynamic, data)

        data = Variant()
        data.set_uint32(4294967294)
        self.create_single_node(addressBranch, "", "uint32",
                                "unit", "description", dynamic, data)

        data = Variant()
        data.set_int64(9223372036854775807)
        self.create_single_node(addressBranch, "", "int64",
                                "unit", "description", dynamic, data)

        data = Variant()
        data.set_uint64(9223372036854775807 * 2)
        self.create_single_node(addressBranch, "", "uint64",
                                "unit", "description", dynamic, data)

        data = Variant()
        data.set_float32(-0.123456789)
        self.create_single_node(addressBranch, "", "float32",
                                "unit", "description", dynamic, data)

        data = Variant()
        data.set_float64(-0.987654321)
        self.create_single_node(addressBranch, "", "float64",
                                "unit", "description", dynamic, data)

        data = Variant()
        data.set_string("This is string")
        self.create_single_node(addressBranch, "", "string",
                                "unit", "description", dynamic, data)

        # Flatbuffers - see samples-python/datalayer.provider/main.py

        data = Variant()
        data.set_array_bool8([False, True, False])
        self.create_single_node(addressBranch, "", "array-of-bool8",
                                "unit", "description", dynamic, data)

        data = Variant()
        data.set_array_int8([-127, -1, 0, 127])
        self.create_single_node(addressBranch, "", "array-of-int8",
                                "unit", "description", dynamic, data)

        data = Variant()
        data.set_array_uint8([0, 127, 128, 255])
        self.create_single_node(addressBranch, "", "array-of-uint8",
                                "unit", "description", dynamic, data)

        data = Variant()
        data.set_array_int16([-32767, -1, 0, 32767])
        self.create_single_node(addressBranch, "", "array-of-int16",
                                "unit", "description", dynamic, data)

        data = Variant()
        data.set_array_uint16([0, 32767, 32768, 65535])
        self.create_single_node(addressBranch, "", "array-of-uint16",
                                "unit", "description", dynamic, data)

        data = Variant()
        data.set_array_int32([-2147483647, -1, 0, 2147483647])
        self.create_single_node(addressBranch, "", "array-of-int32",
                                "unit", "description", dynamic, data)

        data = Variant()
        data.set_array_uint32([0, 2147483647, 2147483648, 4294967295])
        self.create_single_node(addressBranch, "", "array-of-uint32",
                                "unit", "description", dynamic, data)

        data = Variant()
        data.set_array_int64(
            [-9223372036854775807, -1, 0, 9223372036854775807])
        self.create_single_node(addressBranch, "", "array-of-int64",
                                "unit", "description", dynamic, data)
        data = Variant()
        data.set_array_uint64(
            [0, 9223372036854775807, 9223372036854775808, 18446744073709551615])
        self.create_single_node(addressBranch, "", "array-of-uint64",
                                "unit", "description", dynamic, data)

        data = Variant()
        data.set_array_float32([32.1, 32.2, 32.3, 32.4])
        self.create_single_node(addressBranch, "", "array-of-float32",
                                "unit", "description", dynamic, data)

        data = Variant()
        data.set_array_float64([64.1, 64.2, 64.3, 64.4])
        self.create_single_node(addressBranch, "", "array-of-float64",
                                "unit", "description", dynamic, data)

        data = Variant()
        data.set_array_string(["Red", "Green", "Yellow", "Blue"])
        self.create_single_node(addressBranch, "", "array-of-string",
                                "unit", "description", dynamic, data)


    def create_single_node(self, addressBranch: str, addressType : str, name: str, unit: str, description: str, dynamic: bool, data: Variant):
        address = addressBranch + name
        print("Creating", address)

        if is_blank(addressType):
            addressType = "types/datalayer/" + name

        node = ProviderNodeAllData(
            self.provider, addressType, address, name, unit, description, dynamic, data)

        if node is not None:
            self.nodes.append(node)
            self.provider.register_node(address, node.providerNode)


def is_blank (myString):
    return not (myString and myString.strip())