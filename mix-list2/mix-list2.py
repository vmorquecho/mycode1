#!/usr/bin/env python3
proto = ['ssh', 'http', 'https']
protoa = proto
print(proto)
print(protoa)
print(proto[1])
proto.extend('dns') # this line will add
                    # 'd', 'n', and 's' to
                    # the end of out list
print(proto)
proto.append('dns') # this line will add 'dns' to the end out list
#protoa.app
