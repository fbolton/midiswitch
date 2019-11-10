#!/usr/bin/env python

import mido
import time
import platform

class XGNormalVoice:
    PfVoices = [(0, 0), (0, 1), (0, 18), (0, 40), (0, 41), (1, 0), (1, 1), (2, 0), (2, 1), (2, 32), (2, 40), (2, 41), (3, 0), (3, 1), (4, 0), (4, 1), (4, 18), (4, 32), (4, 40), (4, 45), (4, 64), (5, 0), (5, 1), (5, 32), (5, 33), (5, 34), (5, 40), (5, 41), (5, 42), (5, 45), (6, 0), (6, 1), (6, 25), (6, 35), (7, 0), (7, 1), (7, 27), (7, 64), (7, 65)]
    CpVoices = [(8, 0), (9, 0), (10, 0), (10, 64), (11, 0), (11, 1), (11, 45), (12, 0), (12, 1), (12, 64), (12, 97), (12, 98), (13, 0), (14, 0), (14, 96), (14, 97), (15, 0), (15, 35), (15, 96), (15, 97)]
    OrVoices = [(16, 0), (16, 32), (16, 33), (16, 34), (16, 35), (16, 36), (16, 37), (16, 38), (16, 40), (16, 64), (16, 65), (16, 66), (16, 67), (17, 0), (17, 24), (17, 32), (17, 33), (17, 37), (18, 0), (18, 64), (18, 65), (18, 66), (19, 0), (19, 32), (19, 35), (19, 40), (19, 64), (19, 65), (20, 0), (20, 40), (21, 0), (21, 32), (22, 0), (22, 32), (23, 0), (23, 64)]
    GtVoices = [(24, 0), (24, 16), (24, 25), (24, 43), (24, 96), (25, 0), (25, 16), (25, 35), (25, 40), (25, 41), (25, 96), (26, 0), (26, 18), (26, 32), (26, 96), (27, 0), (27, 32), (27, 65), (27, 66), (28, 0), (28, 40), (28, 41), (28, 43), (28, 45), (28, 96), (29, 0), (29, 43), (30, 0), (30, 12), (30, 24), (30, 35), (30, 36), (30, 37), (30, 38), (30, 40), (30, 41), (30, 43), (30, 45), (31, 0), (31, 65), (31, 66)]
    BaVoices = [(32, 0), (32, 40), (32, 45), (33, 0), (33, 18), (33, 27), (33, 40), (33, 43), (33, 45), (33, 64), (33, 65), (33, 112), (34, 0), (34, 28), (35, 0), (35, 32), (35, 33), (35, 34), (35, 96), (35, 97), (36, 0), (36, 27), (36, 32), (36, 64), (36, 65), (37, 0), (37, 43), (38, 0), (38, 18), (38, 20), (38, 24), (38, 27), (38, 35), (38, 40), (38, 64), (38, 65), (38, 66), (38, 67), (38, 68), (38, 96), (38, 112), (38, 113), (39, 0), (39, 6), (39, 12), (39, 18), (39, 19), (39, 32), (39, 40), (39, 41), (39, 64), (39, 65), (39, 66), (39, 67), (39, 112), (39, 113), (39, 114)]
    StVoices = [(40, 0), (40, 8), (41, 0), (42, 0), (43, 0), (44, 0), (44, 8), (44, 40), (45, 0), (46, 0), (46, 40), (47, 0)]
    EnVoices = [(48, 0), (48, 3), (48, 8), (48, 24), (48, 35), (48, 40), (48, 41), (48, 42), (48, 45), (49, 0), (49, 3), (49, 8), (49, 40), (49, 41), (49, 64), (49, 65), (50, 0), (50, 27), (50, 64), (50, 65), (51, 0), (52, 0), (52, 3), (52, 16), (52, 32), (52, 40), (53, 0), (54, 0), (54, 40), (54, 41), (54, 64), (55, 0), (55, 35), (55, 64), (55, 68), (55, 70), (55, 71), (55, 72), (55, 73)]
    BrVoices = [(56, 0), (56, 16), (56, 17), (56, 32), (57, 0), (57, 18), (58, 0), (58, 16), (59, 0), (60, 0), (60, 6), (60, 32), (60, 37), (61, 0), (61, 3), (61, 35), (61, 40), (61, 41), (61, 42), (62, 0), (62, 12), (62, 20), (62, 24), (62, 27), (62, 32), (62, 40), (62, 45), (62, 64), (63, 0), (63, 18), (63, 40), (63, 41), (63, 45), (63, 64)]
    RdVoices = [(64, 0), (65, 0), (65, 40), (65, 43), (66, 0), (66, 40), (66, 41), (66, 64), (67, 0), (68, 0), (69, 0), (70, 0), (71, 0)]
    PiVoices = [(72, 0), (73, 0), (74, 0), (75, 0), (76, 0), (77, 0), (78, 0), (79, 0)]
    LdVoices = [(80, 0), (80, 6), (80, 8), (80, 18), (80, 19), (80, 64), (80, 65), (80, 66), (80, 67), (81, 0), (81, 6), (81, 8), (81, 18), (81, 19), (81, 20), (81, 24), (81, 25), (81, 27), (81, 32), (81, 35), (81, 36), (81, 40), (81, 41), (81, 45), (81, 64), (81, 96), (82, 0), (82, 65), (83, 0), (83, 64), (83, 65), (84, 0), (84, 64), (84, 65), (84, 66), (85, 0), (85, 24), (85, 64), (86, 0), (86, 35), (87, 0), (87, 16), (87, 64), (87, 65)]
    PdVoices = [(88, 0), (88, 64), (89, 0), (89, 16), (89, 17), (89, 18), (89, 64), (89, 65), (90, 0), (90, 64), (90, 65), (90, 66), (90, 67), (91, 0), (91, 64), (91, 66), (91, 67), (92, 0), (92, 64), (92, 65), (93, 0), (93, 64), (93, 65), (94, 0), (95, 0), (95, 20), (95, 27), (95, 64), (95, 66)]
    FxVoices = [(96, 0), (96, 45), (96, 64), (96, 65), (96, 66), (97, 0), (97, 27), (97, 64), (98, 0), (98, 12), (98, 14), (98, 18), (98, 35), (98, 40), (98, 41), (98, 42), (98, 64), (98, 65), (98, 66), (98, 67), (98, 68), (98, 69), (98, 70), (98, 71), (98, 72), (99, 0), (99, 18), (99, 19), (99, 40), (99, 64), (99, 65), (99, 66), (99, 67), (100, 0), (100, 64), (100, 96), (101, 0), (101, 64), (101, 65), (101, 66), (101, 67), (101, 68), (101, 70), (101, 71), (101, 96), (102, 0), (102, 8), (102, 14), (102, 64), (102, 65), (102, 66), (102, 67), (102, 68), (102, 69), (103, 0), (103, 64)]
    EtVoices = [(104, 0), (104, 32), (104, 35), (104, 96), (104, 97), (105, 0), (105, 28), (105, 96), (105, 97), (105, 98), (106, 0), (107, 0), (107, 96), (107, 97), (108, 0), (109, 0), (110, 0), (111, 0), (111, 64), (111, 96), (111, 97)]
    PcVoices = [(112, 0), (112, 96), (112, 97), (112, 98), (112, 99), (112, 100), (112, 101), (113, 0), (114, 0), (114, 97), (114, 98), (115, 0), (115, 96), (116, 0), (116, 96), (117, 0), (117, 64), (117, 65), (117, 66), (118, 0), (118, 64), (118, 65), (119, 0)]
    SeVoices = [(120, 0), (121, 0), (122, 0), (123, 0), (124, 0), (125, 0), (126, 0), (127, 0)]
    AllVoices = [PfVoices, CpVoices, OrVoices, GtVoices, BaVoices, StVoices, EnVoices, BrVoices, RdVoices, PiVoices, LdVoices, PdVoices, FxVoices, EtVoices, PcVoices, SeVoices]

    def __init__(self):
        pass

    def lookup(self, program_group, bank_lsb):
        # Returns a tuple: (program_number, bank_lsb)
        voice_group = XGNormalVoice.AllVoices[program_group]
        group_len = len(voice_group)
        return voice_group[bank_lsb % group_len]

    def program_group_len(self, program_group):
        voice_group = XGNormalVoice.AllVoices[program_group]
        return len(voice_group)


class ProxyPort:
    def __init__(self, port=None):
        self.port = port

    def send(self, msg):
        if self.port is not None:
            self.port.send(msg)

    def set_port(self, port):
        self.port = port

    def get_port(self):
        return self.port

    def is_none(self):
        return self.port is None


class PortManager:
    """Keeps track of Midi ports as they are plugged in and out"""
    MIDI_ADAPTER_CABLE = "USB MIDI Interface MIDI 1"
    NOVATION_REMOTE_37SL_1 = "ReMOTE SL MIDI 1"
    NOVATION_REMOTE_37SL_2 = "ReMOTE SL MIDI 2"
    NOVATION_REMOTE_37SL_3 = "ReMOTE SL MIDI 3"
    BEATSTEP_PRO_1 = "Arturia BeatStep Pro MIDI 1"
    BEATSTEP_PRO_2 = "Arturia BeatStep Pro MIDI 2"
    KEYSTEP = "Arturia KeyStep 32 MIDI 1"
    YAMAHA_P45 = "Digital Piano MIDI 1"
    MODEL_D = "MODEL D MIDI 1"
    BLOFELD = "Blofeld MIDI 1"
    NOVATION_PEAK = "Peak MIDI 1"
    MIDIFACE_4x4_1 = "MIDI4x4 MIDI 1"
    MIDIFACE_4x4_2 = "MIDI4x4 MIDI 2"
    MIDIFACE_4x4_3 = "MIDI4x4 MIDI 3"
    MIDIFACE_4x4_4 = "MIDI4x4 MIDI 4"
    ANALOG_FOUR = "Elektron Analog Four MIDI 1"
    ROLAND_RD_2000 = "RD-2000 MIDI 1"
    BEHRINGER_K2 = "K-2 MIDI 1"


    def __init__(self):
        self.active_inputs = {}
        self.from_endpoints = {}
        self.proxy_ports = {}
        self.router_rules = []

    def activate_input(self, portName):
        print "Dectected new input: " + portName
        if portName in self.from_endpoints:
            self.active_inputs[portName] = mido.open_input(portName)
            print "Activated input: " + portName

    def activate_output(self, portName):
        print "Detected new output: " + portName
        # print self.proxy_ports
        if portName in self.proxy_ports:
            self.proxy_ports[portName].set_port(mido.open_output(portName))
            print "Activated output: " + portName

    def deactivate_input(self, portName):
        print "Unplugged input: " + portName
        if portName in self.active_inputs:
            self.active_inputs[portName].close()
            del(self.active_inputs[portName])
            print "Deactivated input: " + portName

    def deactivate_output(self, portName):
        print "Unplugged output: " + portName
        if portName in self.proxy_ports:
            self.proxy_ports[portName].get_port().close()
            self.proxy_ports[portName].set_port(None)
            print "Deactivated output: " + portName

    def register_from(self, portName, rule):
        if portName not in self.from_endpoints:
            # Create an empty list of registered routes for portName
            self.from_endpoints[portName] = []
        self.from_endpoints[portName].append(rule)

    def get_proxy_port(self, portName):
        if portName in self.proxy_ports:
            return self.proxy_ports[portName]
        else:
            proxy = ProxyPort()
            self.proxy_ports[portName] = proxy
            return proxy

    def dispatch_pending_messages(self):
        for port_name in self.active_inputs:
            input_port = self.active_inputs[port_name]
            rule_list = self.from_endpoints[port_name]
            for msg in input_port.iter_pending():
                for rule in rule_list:
                    if rule.matches(msg, port_name):
                        # Try to avoid stuck notes
                        if (msg.type=='note_off') or (msg.type=='note_on' and int(msg.velocity)==0):
                            time.sleep(0.001)
                        rule.send(msg)
                        break # Match one rule only

    def addRule(self, fromPortList, toPort, msgMatcher, sysexMatcher, msgMapper, router):
        self.router_rules.append(RouterRule(self, fromPortList, toPort, msgMatcher, sysexMatcher, msgMapper, router))


class RouterRule:
    def __init__(self, port_manager, fromPortList, toPort, msgMatcher, sysexMatcher, msgMapper, router):
        self.port_manager = port_manager
        if isinstance(fromPortList, basestring):
            # Make sure that 'fromPortList' actually is a list
            fromPortList = [fromPortList]
        self.fromPortList = fromPortList
        self.toPort = toPort
        self.msgMatcher = msgMatcher
        self.sysexMatcher = sysexMatcher
        self.msgMapper = msgMapper
        self.router = router
        # Register ports
        for fromPort in self.fromPortList:
            self.port_manager.register_from(fromPort, self)
        self.toPortProxy = self.port_manager.get_proxy_port(self.toPort)

    def is_system_common_message(self, msg):
        # A Midi system common message has *no* associated Midi channel
        # and its first byte always has the form 0xFn
        return msg.bytes()[0] & 0xF0 == 0xF0

    def matches(self, msg, fromPort):
        if self.toPortProxy.is_none():
            # Skip rule, if output port is disabled
            return False
        if fromPort in self.fromPortList:
            if not self.is_system_common_message(msg):
                # Messages with a well-defined channel
                if self.msgMatcher is None:
                    return False
                else:
                    return self.msgMatcher.matches(msg)
            else:
                # System common messages messages (including sysex)
                if self.sysexMatcher is None:
                    return False
                else:
                    return self.sysexMatcher.matches(msg)
        else:
            return False

    def send(self, msg):
        if self.msgMapper is not None:
            # print "Before msg map: " + str(msg)
            msg = self.msgMapper.map(msg)
            # print "After msg map: " + str(msg)
        self.router.send(msg, self.toPortProxy)


class ChannelMatcher:
    def __init__(self, chan, chanMax = None):
        self.chan = chan
        self.chanMax = chanMax

    def matches(self, msg):
        if self.chanMax is None:
            return msg.channel == self.chan
        else:
            return (self.chan <= msg.channel) and (msg.channel <= self.chanMax)


class SysexDevice:
    def __init__(self, deviceID):
        self.deviceID = deviceID

    def matches(self, msg):
        return msg.bytes()[1] == self.deviceID


class ChannelMapper:
    def __init__(self, chanMapFunction):
        self.chanMapFunction = chanMapFunction

    def map(self, msg):
        msg.channel = self.chanMapFunction(int(msg.channel))
        return msg


class CCtoNoteMapper:
    def __init__(self):
        self.cc_to_note = {20:73, 21:75,       23:78, 24:80, 25:82,
                        28:72, 29:74, 30:76, 31:77, 52:79, 53:81, 54:83, 55:84}

    def map(self, msg):
        if msg.type == 'control_change':
            cc = int(msg.control)
            chan = int(msg.channel)
            value = int(msg.value)
            if cc in self.cc_to_note:
                note = self.cc_to_note[cc]
                if value == 127:
                    # 127 => Note on
                    byte_list = [0x90|chan, note, 100]
                    msg = mido.parse(byte_list)
                else:
                    # 0 => Note off
                    byte_list = [0x80|chan, note, 100]
                    msg = mido.parse(byte_list)
        return msg


class RouterThru:
    def send(self, msg, toPortProxy):
        # print msg
        toPortProxy.send(msg)


class RouterWithKeyboardSplit:
    def __init__(self):
        self.note_60_borrow = False
        self.note_36_borrow = False
        self.note_72_borrow = False
        self.note_84_borrow = False
        self.channel_map =\
            {0: [0], 1: [1, 0], 2: [2, 1, 0], 3: [3, 2, 1, 0], 4: [4], 5: [5, 4], 6: [6, 5, 4], 7: [7, 6, 5, 4],
             8: [8], 9: [9, 8], 10: [10, 9, 8], 11: [11, 10, 9, 8], 12: [12], 13: [13, 12], 14: [14, 13, 12], 15: [15, 14, 13, 12]}

    def is_system_common_message(self, msg):
        # A Midi system common message has *no* associated Midi channel
        # and its first byte always has the form 0xFn
        return msg.bytes()[0] & 0xF0 == 0xF0

    def send_to_channel(self, msg, toPortProxy, chan):
        byte_list = msg.bytes()
        # Replace original channel with 'chan'
        byte_list[0] = (byte_list[0] & 0xF0) | chan
        toPortProxy.send(mido.parse(byte_list))
        return

    def send(self, msg, toPortProxy):
        if self.is_system_common_message(msg):
            # Ignore system common messages
            return
        in_chan = int(msg.channel)
        chan_list = self.channel_map[in_chan]
        if not (msg.type=='note_on' or msg.type=='note_off'):
            # Default behaviour: send to all channels in split
            # (for example, sustain pedal messages)
            for out_chan in chan_list:
                self.send_to_channel(msg, toPortProxy, out_chan)
            return
        else:
            split_size = len(chan_list)
            note = int(msg.note)
            if split_size==1:
                # No split => use whole keyboard
                self.send_to_channel(msg, toPortProxy, chan_list[0])
                return
            elif split_size==2:
                # 2-fold split
                # Split at middle C = 60
                if note<60 or (note==60 and self.note_60_borrow):
                    if 55<=note:
                        self.note_60_borrow = True
                    msg.note = int(msg.note) + 24  # Transpose up by two octaves
                    self.send_to_channel(msg, toPortProxy, chan_list[0])
                else:
                    self.note_60_borrow = False
                    msg.note = int(msg.note) - 24  # Transpose down by two octaves
                    self.send_to_channel(msg, toPortProxy, chan_list[1])
                return
            elif split_size==3:
                # 3-fold split
                if note<36 or (note==36 and self.note_36_borrow):
                    if 31<=note:
                        self.note_36_borrow = True
                    msg.note = int(msg.note) + 12  # Transpose up by one octave
                    self.send_to_channel(msg, toPortProxy, chan_list[0])
                elif note<72 or (note==72 and self.note_72_borrow):
                    self.note_36_borrow = False
                    if 67<=note:
                        self.note_72_borrow = True
                    self.send_to_channel(msg, toPortProxy, chan_list[1])
                else:
                    self.note_72_borrow = False
                    msg.note = int(msg.note) - 24  # Transpose down by two octaves
                    self.send_to_channel(msg, toPortProxy, chan_list[2])
                return
            elif split_size==4:
                # 4-fold split
                if note<36 or (note==36 and self.note_36_borrow):
                    if 31<=note:
                        self.note_36_borrow = True
                    msg.note = int(msg.note) + 12  # Transpose up by one octave
                    self.send_to_channel(msg, toPortProxy, chan_list[0])
                elif note<60 or (note==60 and self.note_60_borrow):
                    self.note_36_borrow = False
                    if 55<=note:
                        self.note_60_borrow = True
                    self.send_to_channel(msg, toPortProxy, chan_list[1])
                elif note<84 or (note==84 and self.note_84_borrow):
                    self.note_60_borrow = False
                    if 79<=note:
                        self.note_84_borrow = True
                    self.send_to_channel(msg, toPortProxy, chan_list[2])
                else:
                    self.note_84_borrow = False
                    msg.note = int(msg.note) - 24  # Transpose down by two octaves
                    self.send_to_channel(msg, toPortProxy, chan_list[3])
                return


class RouterCCtoNote:
    def __init__(self):
        self.mapper = CCtoNoteMapper()

    def send(self, msg, toPortProxy):
        # print msg
        toPortProxy.send(self.mapper.map(msg))

class RouterToModelD:
    def __init__(self):
        pass

    def send(self, msg, toPortProxy):
        if msg.type=='control_change' and (20<=msg.control and msg.control<=22) and msg.value == 127:
            # Change the key priority
            key_priority = int(msg.control) - 20
            byte_list = [0xF0, 0x00, 0x20, 0x32, 0x00, 0x7F, 0x0A, 0x01, 0x00, key_priority, 0xF7]
            # print byte_list
            toPortProxy.send(mido.parse(byte_list))
            return
        if msg.type=='control_change' and (28<=msg.control and msg.control<=29) and msg.value == 127:
            # Change multi trigger option
            multi_trigger = int(msg.control) - 28
            byte_list = [0xF0, 0x00, 0x20, 0x32, 0x00, 0x7F, 0x0A, 0x02, 0x00, multi_trigger, 0xF7]
            # print byte_list
            toPortProxy.send(mido.parse(byte_list))
            return
        # print msg
        toPortProxy.send(msg)



class RouterQY100:
    def __init__(self):
        self.part = 0
        self.program_group = 0
        self.xg = XGNormalVoice()

    def send(self, msg, toPortProxy):
        # print msg
        if msg.type=='note_on' or msg.type=='note_off' or msg.type=='aftertouch':
            msg.channel = self.part
        if msg.type=='control_change' and msg.control==123:
            self.part = int(msg.channel)
            return
        if msg.type=='control_change' and msg.control==0:
            # Bank select MSB
            # Novation controller always sends MSB = 0
            # Swallow this message
            return
        if msg.type=='control_change' and msg.control==32:
            # Bank select LSB
            # Novation controller sends LSB in range 0..127
            # print "Bank LSB = " + str(msg.value)
            (program, bank_lsb) = self.xg.lookup(self.program_group, msg.value)
            # print "(program, bank_lsb) = " + str(program) + ", " + str(bank_lsb)
            msg = mido.Message('control_change', channel=self.part, control=0, value=0)
            toPortProxy.send(msg)
            msg = mido.Message('control_change', channel=self.part, control=32, value=bank_lsb)
            toPortProxy.send(msg)
            msg = mido.Message('program_change', channel=self.part, program=program)
            toPortProxy.send(msg)
            return
        if msg.hex().startswith('F0 43 10 4C 08'):
            # Sysex messages for controlling QY100 parts
            byte_list = msg.bytes()
            byte_list[5] = self.part
            if byte_list[6]==3:
                # Part program change (Sysex) message
                # detect special values for changing program group
                data = byte_list[7]
                if data%8==0:
                    self.program_group = data / 8
            msg = mido.parse(byte_list)
        if msg.type=='program_change':
            byte_list = msg.bytes()
            byte_list[1] = self.program_group * 8 + byte_list[1]%8
            msg = mido.parse(byte_list)
        toPortProxy.send(msg)


class RouterBeatStepPro2QY100:
    def __init__(self):
        self.note_mapper = CCtoNoteMapper()
        self.xg = XGNormalVoice()
        self.value_list_allchannels = []
        self.value_list_defaults = [64, 64, 64,  64,  64, 64, 64, 64,
                                    64,  0, 40, 127, 100, 64,  0,  0]
        self.sysex_codes = [
                            0x18, # FltCut
                            0x1a, # AtkTim
                            0x1b, # DecTim
                            0x1c, # RelTim
                            0x69, # PEG InitLvl
                            0x6a, # PEG AtkTim
                            0x6b, # PEG RelLvl
                            0x6c, # PEG RelTim
                            0x19, # FltRes
                            0x12, # ChoSnd
                            0x13, # RvbSnd
                            0x11, # DryLvl
                            0x0b, # Vol
                            0x08  # Note shift -24..+24 semitone
                            ]
        for k in range(16):
            # Need to do a deep copy here!
            self.value_list_allchannels.append(self.value_list_defaults[:])

    def increment_value(self, val, inc, max_val=127):
        if inc >= 0:
            return min(val + inc, max_val)
        else:
            return max(val + inc, 0)

    def send(self, msg, toPortProxy):
        # print msg
        if msg.type!='control_change':
            # Pass through by default, for non-CC messages
            toPortProxy.send(msg)
            return
        if msg.type=='control_change' and (int(msg.value) - 64)==0:
            # Zero increment => do nothing!
            return
        if msg.type=='control_change' and ((msg.control>=102 and msg.control<=115)):
            knob_index = int(msg.control) - 102
            chan = int(msg.channel)
            sysex_code = self.sysex_codes[knob_index]
            value_list = self.value_list_allchannels[chan]
            new_val = self.increment_value(value_list[knob_index], int(msg.value) - 64)
            value_list[knob_index] = new_val
            byte_list = [0xF0, 0x43, 0x10, 0x4c, 0x08, chan, sysex_code, new_val, 0xF7]
            # print byte_list
            toPortProxy.send(mido.parse(byte_list))
            return
        if msg.type=='control_change' and msg.control==116:
            knob_index = int(msg.control) - 102
            chan = int(msg.channel)
            value_list = self.value_list_allchannels[chan]
            # Program
            program_group = self.increment_value(value_list[knob_index], int(msg.value) - 64, max_val=15)
            value_list[knob_index] = program_group
            # Reset the Bank LSB to zero also
            value_list[knob_index+1] = 0
            msg = mido.Message('control_change', channel=chan, control=0, value=0)
            toPortProxy.send(msg)
            msg = mido.Message('control_change', channel=chan, control=32, value=0)
            toPortProxy.send(msg)
            msg = mido.Message('program_change', channel=chan, program=program_group * 8)
            toPortProxy.send(msg)
            return
        if msg.type=='control_change' and msg.control==117:
            knob_index = int(msg.control) - 102
            chan = int(msg.channel)
            value_list = self.value_list_allchannels[chan]
            # Bank select LSB
            program_group = value_list[knob_index-1]
            group_len = self.xg.program_group_len(program_group)
            new_val = self.increment_value(value_list[knob_index], int(msg.value) - 64, max_val= group_len - 1)
            value_list[knob_index] = new_val
            (program, bank_lsb) = self.xg.lookup(program_group, new_val)
            # print "(program, bank_lsb) = " + str(program) + ", " + str(bank_lsb)
            msg = mido.Message('control_change', channel=chan, control=0, value=0)
            toPortProxy.send(msg)
            msg = mido.Message('control_change', channel=chan, control=32, value=bank_lsb)
            toPortProxy.send(msg)
            msg = mido.Message('program_change', channel=chan, program=program)
            toPortProxy.send(msg)
            return
        #else
        toPortProxy.send(self.note_mapper.map(msg))


def main():
    if platform.linux_distribution()[0]=='Fedora':
        OS_FEDORA = True
    else:
        OS_FEDORA = False
    active_input_names = set()
    active_output_names = set()
    manager = PortManager()
    manager.addRule(
        [manager.BEATSTEP_PRO_1, manager.KEYSTEP, manager.MIDI_ADAPTER_CABLE, manager.ROLAND_RD_2000], # List of incoming ports
        manager.MIDIFACE_4x4_1, # Outgoing port
        ChannelMatcher(12), # Route channel 13 (=12+1) to OUT port 1 of Midiface 4x4
        None, # No sysex matcher
        ChannelMapper(lambda x: 0), # Map messages to channel 1 by default
        RouterThru()
    )
    manager.addRule(
        [manager.BEATSTEP_PRO_1, manager.KEYSTEP, manager.MIDI_ADAPTER_CABLE, manager.ROLAND_RD_2000], # List of incoming ports
        manager.MIDIFACE_4x4_2, # Outgoing port
        ChannelMatcher(13), # Route channel 14 (=13+1) to OUT port 2 of Midiface 4x4
        None, # No sysex matcher
        ChannelMapper(lambda x: 0), # Map messages to channel 1 by default
        RouterThru()
    )
    manager.addRule(
        [manager.BEATSTEP_PRO_1, manager.KEYSTEP, manager.MIDI_ADAPTER_CABLE, manager.ROLAND_RD_2000], # List of incoming ports
        manager.MIDIFACE_4x4_3, # Outgoing port
        ChannelMatcher(14), # Route channel 15 (=14+1) to OUT port 3 of Midiface 4x4
        None, # No sysex matcher
        ChannelMapper(lambda x: 0), # Map messages to channel 1 by default
        RouterThru()
    )
    manager.addRule(
        [manager.BEATSTEP_PRO_1, manager.KEYSTEP, manager.MIDI_ADAPTER_CABLE, manager.ROLAND_RD_2000], # List of incoming ports
        manager.MIDIFACE_4x4_4, # Outgoing port
        ChannelMatcher(15), # Route channel 16 (=15+1) to OUT port 4 of Midiface 4x4
        None, # No sysex matcher
        ChannelMapper(lambda x: 0), # Map messages to channel 1 by default
        RouterThru()
    )
    manager.addRule(
        [manager.BEATSTEP_PRO_1, manager.KEYSTEP, manager.MIDI_ADAPTER_CABLE, manager.ROLAND_RD_2000], # List of incoming ports
        manager.ANALOG_FOUR, # Outgoing port
        ChannelMatcher(5), # Route channel 6 (=5+1) to the Elektron Analog Four
        None, # No sysex matcher
        ChannelMapper(lambda x: 1), # Map Analog Four messages to channel 9 (auto channel)
        RouterThru()
    )
    manager.addRule(
        [manager.BEATSTEP_PRO_1, manager.KEYSTEP, manager.MIDI_ADAPTER_CABLE, manager.ROLAND_RD_2000], # List of incoming ports
        manager.NOVATION_PEAK, # Outgoing port
        ChannelMatcher(6), # Route channel 7 (=6+1) to the Novation Peak
        None, # No sysex matcher
        ChannelMapper(lambda x: 0), # Map Peak messages to channel 1
        RouterThru()
    )
    manager.addRule(
        [manager.BEATSTEP_PRO_1, manager.KEYSTEP, manager.MIDI_ADAPTER_CABLE, manager.ROLAND_RD_2000], # List of incoming ports
        manager.BEHRINGER_K2, # Outgoing port
        ChannelMatcher(7), # Route channel 8 (=7+1) to the Behringer K-2
        None, # No sysex matcher
        ChannelMapper(lambda x: 0), # Map K-2 messages to channel 1
        RouterThru()
    )
    manager.addRule(
        [manager.BEATSTEP_PRO_1, manager.KEYSTEP, manager.MIDI_ADAPTER_CABLE, manager.ROLAND_RD_2000], # List of incoming ports
        manager.MODEL_D, # Outgoing port
        ChannelMatcher(8), # Route channel 9 (=8+1) to the Model D
        None, # No sysex matcher
        ChannelMapper(lambda x: 0), # Map Model D messages to channel 1
        RouterToModelD()
    )
    manager.addRule(
        [manager.BEATSTEP_PRO_1, manager.KEYSTEP, manager.MIDI_ADAPTER_CABLE, manager.ROLAND_RD_2000], # List of incoming ports
        manager.BLOFELD, # Outgoing port
        ChannelMatcher(10, 15), # Route channels 11-16 to the Blofeld
        None, # No sysex matcher
        ChannelMapper(lambda x: x - 10), # Map Blofeld messages to channels 1-6
        RouterCCtoNote()
    )
    manager.addRule(
        [manager.BEATSTEP_PRO_1, manager.MIDI_ADAPTER_CABLE], # List of incoming ports
        manager.ROLAND_RD_2000, # Outgoing port for RD-2000
        ChannelMatcher(0, 15), # Route all channels to the RD-2000
        None, # No sysex matcher
        None, # No channel mapper
        RouterThru()
    )
    manager.addRule(
        manager.KEYSTEP, # List of incoming ports
        manager.ROLAND_RD_2000, # Outgoing port for RD-2000
        ChannelMatcher(3, 15), # Block channels 1, 2, and 3, used to control the Beatstep Pro
        None, # No sysex matcher
        None, # No channel mapper
        RouterThru()
    )
    manager.addRule(
        [manager.BEATSTEP_PRO_1, manager.MIDI_ADAPTER_CABLE], # List of incoming ports
        manager.MIDI_ADAPTER_CABLE, # Outgoing port for QY100
        ChannelMatcher(0, 15), # Route all channels to the QY100
        None, # No sysex matcher
        None, # No channel mapper
        RouterBeatStepPro2QY100()
    )
    manager.addRule(
        manager.KEYSTEP, # List of incoming ports
        manager.MIDI_ADAPTER_CABLE, # Outgoing port for QY100
        ChannelMatcher(3, 15), # Block channels 1, 2, and 3, used to control the Beatstep Pro
        None, # No sysex matcher
        None, # No channel mapper
        RouterBeatStepPro2QY100()
    )
    manager.addRule(
        manager.NOVATION_REMOTE_37SL_1, # List of incoming ports
        manager.MIDI_ADAPTER_CABLE, # Outgoing port for QY100
        ChannelMatcher(0, 15), # Route all channels to the QY100
        SysexDevice(0x43), # Match sysex messages with ID = 0x43
        None, # No channel mapper
        RouterQY100()
    )
    while True:
        # Update input ports
        raw_input_names = mido.get_input_names()
        if OS_FEDORA:
            input_names = set(
                map(lambda x:x.rsplit(' ', 1)[0].split(':')[1], raw_input_names)
            )
        else:
            input_names = set(raw_input_names)
        input_names_to_activate = input_names - active_input_names
        for name in input_names_to_activate:
            manager.activate_input(name)
        input_names_to_deactivate = active_input_names - input_names
        for name in input_names_to_deactivate:
            manager.deactivate_input(name)
        active_input_names = input_names
        # Update output ports
        raw_output_names = mido.get_output_names()
        if OS_FEDORA:
            output_names = set(
                map(lambda x: x.rsplit(' ', 1)[0].split(':')[1], raw_output_names)
            )
        else:
            output_names = set(raw_output_names)
        output_names_to_activate = output_names - active_output_names
        for name in output_names_to_activate:
            manager.activate_output(name)
        output_names_to_deactivate = active_output_names - output_names
        for name in output_names_to_deactivate:
            manager.deactivate_output(name)
        active_output_names = output_names
        # Let's process some messages now
        for k in range(1000):
            manager.dispatch_pending_messages()
        # Wait for a second...
        # time.sleep(0.5)


main()
