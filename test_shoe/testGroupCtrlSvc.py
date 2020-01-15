##########################################################################
#SHOE - An open source HEOS configuration and control project
#Copyright (C) 2020  Mike Karasoff, mike@karatronics.com
#
#testGroupCtrlSvc.py
#Class for unittest data generated from GroupControl service SCPD file.
#
#
##########################################################################
#GPLv.3 License
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
############################################################################

from .shoeTestXml import ShoeTestXml
from collections import OrderedDict

class TestGroupCtrlSvc(ShoeTestXml):
    def __init__(self):
        xmlFile='GroupControl.xml'
        md5hex='d2164658e60eedbe0c79090ceb1d904e'
        self.urlPath='/upnp/scpd/AiosServicesDvc/'
        self.urn='urn:schemas-denon-com:service:GroupControl:1'
        self.name='GroupControl'
        self.devName='AiosServices'

        self.url='%s%s' % (self.urlPath, xmlFile)
        super(TestGroupCtrlSvc, self).__init__(xmlFile, md5hex)

################################################################################
        self.getGroupVolCmnd='GetGroupVolume'

        self.getGroupVolArg= [\
                            {'relatedStateVariable': 'GroupUUID', 'direction': 'in', 'name': 'GroupUUID',\
                             'state' : {'dataType': 'string', '@sendEvents': 'no', 'name': 'GroupUUID'}},\
                            {'relatedStateVariable': 'GroupVolume', 'direction': 'out','name': 'GroupVolume',\
                             'state' : {'dataType': 'ui2', 'defaultValue': '0', \
                             'allowedValueRange': {'step': '1', 'minimum': '0', 'maximum': '100'}, \
                             'name': 'GroupVolume', '@sendEvents': 'no'}},]

        getGroupVolRtnBody = '<u:GetGroupVolumeResponse  xmlns:u="urn:schemas-denon-com:service:GroupControl:1">'\
                               '<GroupVolume>90</GroupVolume></u:GetGroupVolumeResponse>'

        self.getGroupVolRtnXml ='%s%s%s' % (self.xmlRtnHead, getGroupVolRtnBody, self.xmlRtnTail)

        self.getGroupVolRtn=OrderedDict([('GroupVolume', 90),])

################################################################################
        self.createGroupCmnd='CreateGroup'

        self.createGroupHdr={'HOST': '127.0.0.1:60006', \
                            'CONTENT-LENGTH': '439', \
                            'Accept-Ranges': 'bytes', \
                            'CONTENT-TYPE': 'text/xml; charset="utf-8"', \
                            'SOAPACTION': '"urn:schemas-denon-com:service:GroupControl:1#CreateGroup"', \
                            'USER-AGENT': 'LINUX UPnP/1.0 Denon-Heos/149200'}

        self.createGroupCmndXml= '<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" '\
                                    's:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">'\
                                    '<s:Body>'\
                                    '<u:CreateGroup xmlns:u="urn:schemas-denon-com:service:GroupControl:1">'\
                                        '<GroupFriendlyName>Jam</GroupFriendlyName>'\
                                        '<GroupMemberUUIDList>caf7916a94db1a1300800005cdfbb9c6,'\
                                           'f3ddb59f3e691f1e00800005cdff1706</GroupMemberUUIDList>'\
                                        '<GroupMemberChannelList></GroupMemberChannelList>'\
                                    '</u:CreateGroup>'\
                                    '</s:Body>'\
                                    '</s:Envelope>'

        self.createGroupArg=  [\
                {'relatedStateVariable': 'GroupFriendlyName','direction': 'in',\
                  'name': 'GroupFriendlyName',\
                  'state' : {'dataType': 'string', '@sendEvents': 'no', 'name': 'GroupFriendlyName'}},\
                {'relatedStateVariable': 'GroupMemberUUIDList', 'direction': 'in',\
                  'name': 'GroupMemberUUIDList',\
                  'state' :{'dataType': 'string', '@sendEvents': 'no', 'name': 'GroupMemberUUIDList'}},\
                {'relatedStateVariable': 'GroupMemberChannelList', 'direction': 'in', \
                  'name': 'GroupMemberChannelList',\
                  'state' : {'dataType': 'string', '@sendEvents': 'no', 'name': 'GroupMemberChannelList'}},\
                {'relatedStateVariable': 'GroupUUID', 'direction': 'out', \
                   'name': 'GroupUUID',\
                   'state' : {'dataType': 'string', '@sendEvents': 'no', 'name': 'GroupUUID'}},]

        createGroupRtnBody = '<u:CreateGroupResponse  xmlns:u="urn:schemas-denon-com:service:GroupControl:1">'\
                               '<GroupUUID>17083c46d003001000800005cdfbb9c6</GroupUUID></u:CreateGroupResponse>'

        self.createGroupRtnXml ='%s%s%s' % (self.xmlRtnHead, createGroupRtnBody, self.xmlRtnTail)

        print(self.createGroupRtnXml)

        self.createGroupRtn=OrderedDict([('GroupUUID', '17083c46d003001000800005cdfbb9c6'),])

################################################################################
        self.getCurrStCmnd='GetCurrentState'

        self.getCurrStArg= [\
                            {'relatedStateVariable': 'LastChange', 'direction': 'out', 'name': 'CurrentState',\
                             'state' : {'dataType': 'string', '@sendEvents': 'yes', 'name': 'LastChange'}},]

        self.getCurrStHdr={'HOST': '127.0.0.1:60006', \
                            'CONTENT-LENGTH': '239', \
                            'Accept-Ranges': 'bytes', \
                            'CONTENT-TYPE': 'text/xml; charset="utf-8"', \
                            'SOAPACTION': '"urn:schemas-denon-com:service:GroupControl:1#GetCurrentState"', \
                            'USER-AGENT': 'LINUX UPnP/1.0 Denon-Heos/149200'}

        self.getCurrStCmndXml= '<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" '\
                                    's:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">'\
                                    '<s:Body>'\
                                    '<u:GetCurrentState xmlns:u="urn:schemas-denon-com:service:GroupControl:1">'\
                                    '</u:GetCurrentState>'\
                                    '</s:Body>'\
                                    '</s:Envelope>'

        self.getCurrStRtnBody = ''

        self.getCurrStRtnXml='<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" '\
                's:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">'\
                '<s:Body>'\
                    '<u:GetCurrentStateResponse '\
                        'xmlns:u="urn:schemas-denon-com:service:GroupControl:1">'\
                        '<CurrentState>%s</CurrentState></u:GetCurrentStateResponse>'\
                    '</s:Body>'\
                '</s:Envelope>' % self.getCurrStRtnBody

        self.getCurrStRtn=OrderedDict([('CurrentState', None),])
        self.currSt={}
        self.currStFmt=''

################################################################################

        self._cmndTbl={\
            'GetGroupBalance': [\
                {'relatedStateVariable': 'GroupUUID', 'direction': 'in', 'name': 'GroupUUID'},\
                {'relatedStateVariable': 'GroupBalance', 'direction': 'out', 'name': 'GroupBalance'}],\
            'GetGroupTreble': [\
                {'relatedStateVariable': 'GroupUUID', 'direction': 'in', 'name': 'GroupUUID'},\
                {'relatedStateVariable': 'GroupTreble', 'direction': 'out', 'name': 'GroupTreble'}],\
            'GetMediaServerUUID': [\
                {'relatedStateVariable': 'GroupUUID', 'direction': 'in', 'name': 'GroupUUID'},\
                {'relatedStateVariable': 'MediaServerUUID', 'direction': 'out', 'name': 'MediaServerUUID'}],\
            'GetGroupBass': [\
                {'relatedStateVariable': 'GroupUUID', 'direction': 'in', 'name': 'GroupUUID'},\
                {'relatedStateVariable': 'GroupBass', 'direction': 'out', 'name': 'GroupBass'}],\
            'SetGroupMemberChannel': [\
                {'relatedStateVariable': 'GroupUUID', 'direction': 'in', 'name': 'GroupUUID'},\
                {'relatedStateVariable': 'AudioChannel', 'direction': 'in', 'name': 'AudioChannel'}],\
            'GetGroupVolume': [\
                {'relatedStateVariable': 'GroupUUID', 'direction': 'in', 'name': 'GroupUUID'},\
                {'relatedStateVariable': 'GroupVolume', 'direction': 'out', 'name': 'GroupVolume'}],\
            'GetSignalStrength': [\
                {'relatedStateVariable': 'GroupUUID', 'direction': 'in', 'name': 'GroupUUID'},\
                {'relatedStateVariable': 'ExtApSignalStrength', 'direction': 'out', 'name': 'SignalStrength'}],\
            'CreateGroup': [\
                {'relatedStateVariable': 'GroupFriendlyName', 'direction': 'in', 'name': 'GroupFriendlyName'},\
                {'relatedStateVariable': 'GroupMemberUUIDList', 'direction': 'in', 'name': 'GroupMemberUUIDList'},\
                {'relatedStateVariable': 'GroupMemberChannelList', 'direction': 'in', 'name': 'GroupMemberChannelList'},\
                {'relatedStateVariable': 'GroupUUID', 'direction': 'out', 'name': 'GroupUUID'}],\
            'GetGroupStatus': [\
                {'relatedStateVariable': 'GroupUUID', 'direction': 'in', 'name': 'GroupUUID'},\
                {'relatedStateVariable': 'GroupStatus', 'direction': 'out', 'name': 'GroupStatus'}],\
            'GetConfigDeviceUUID': [\
                {'relatedStateVariable': 'GroupUUID', 'direction': 'in', 'name': 'GroupUUID'},\
                {'relatedStateVariable': 'ConfigDeviceUUID', 'direction': 'out', 'name': 'ConfigDeviceUUID'}],\
            'GetGroupMemberList': [\
                {'relatedStateVariable': 'GroupUUID', 'direction': 'in', 'name': 'GroupUUID'},\
                {'relatedStateVariable': 'GroupMemberUUIDList', 'direction': 'out', 'name': 'GroupMemberUUIDList'}],\
            'GetDeviceFriendlyName': [\
                {'relatedStateVariable': 'DeviceFriendlyName', 'direction': 'out', 'name': 'DeviceFriendlyName'}],\
            'AddMembersToGroup': [\
                {'relatedStateVariable': 'GroupUUID', 'direction': 'in', 'name': 'GroupUUID'},\
                {'relatedStateVariable': 'A_ARG_TYPE_IPList', 'direction': 'in', 'name': 'GroupMemberIPList'},\
                {'relatedStateVariable': 'GroupMemberUUIDList', 'direction': 'in', 'name': 'GroupMemberUUIDList'},\
                {'relatedStateVariable': 'GroupMemberChannelList', 'direction': 'in', 'name': 'GroupMemberChannelList'},\
                {'relatedStateVariable': 'GroupUUID', 'direction': 'out', 'name': 'GroupUUIDOut'}],\
            'DummyAction_GroupControl': [\
                {'relatedStateVariable': 'GroupUUID', 'direction': 'in', 'name': 'GroupUUID'},\
                {'relatedStateVariable': 'A_ARG_TYPE_DummyValueGroupControl', 'direction': 'out', 'name': 'DummyValue'}],\
            'SetGroupMute': [\
                {'relatedStateVariable': 'GroupUUID', 'direction': 'in', 'name': 'GroupUUID'},\
                {'relatedStateVariable': 'GroupMute', 'direction': 'in', 'name': 'GroupMute'},\
                {'relatedStateVariable': 'CommandID', 'direction': 'in', 'name': 'CommandID'}],\
            'SetDeviceFriendlyName': [\
                {'relatedStateVariable': 'DeviceFriendlyName', 'direction': 'in', 'name': 'DeviceFriendlyName'}],\
            'GetGroupFriendlyName': [\
                {'relatedStateVariable': 'GroupUUID', 'direction': 'in', 'name': 'GroupUUID'},\
                {'relatedStateVariable': 'GroupFriendlyName', 'direction': 'out', 'name': 'GroupFriendlyName'}],\
            'RemoveMembersFromGroup': [\
                {'relatedStateVariable': 'GroupUUID', 'direction': 'in', 'name': 'GroupUUID'},\
                {'relatedStateVariable': 'GroupMemberUUIDList', 'direction': 'in', 'name': 'GroupMemberUUIDList'}],\
            'GetCurrentState': [\
                {'relatedStateVariable': 'LastChange', 'direction': 'out', 'name': 'CurrentState'}],\
            'SetGroupBalance': [\
                {'relatedStateVariable': 'GroupUUID', 'direction': 'in', 'name': 'GroupUUID'},\
                {'relatedStateVariable': 'GroupBalance', 'direction': 'in', 'name': 'GroupBalance'},\
                {'relatedStateVariable': 'CommandID', 'direction': 'in', 'name': 'CommandID'}],\
            'SetGroupVolume': [\
                {'relatedStateVariable': 'GroupUUID', 'direction': 'in', 'name': 'GroupUUID'},\
                {'relatedStateVariable': 'GroupVolume', 'direction': 'in', 'name': 'GroupVolume'},\
                {'relatedStateVariable': 'CommandID', 'direction': 'in', 'name': 'CommandID'}],\
            'GetGroupMemberChannel': [\
                {'relatedStateVariable': 'GroupUUID', 'direction': 'in', 'name': 'GroupUUID'},\
                {'relatedStateVariable': 'AudioChannel', 'direction': 'out', 'name': 'AudioChannel'}],\
            'GetGroupUpdating': [\
                {'relatedStateVariable': 'GroupUUID', 'direction': 'in', 'name': 'GroupUUID'},\
                {'relatedStateVariable': 'GroupUpdating', 'direction': 'out', 'name': 'GroupUpdating'}],\
            'SetGroupTreble': [\
                {'relatedStateVariable': 'GroupUUID', 'direction': 'in', 'name': 'GroupUUID'},\
                {'relatedStateVariable': 'GroupTreble', 'direction': 'in', 'name': 'GroupTreble'}],\
            'SetGroupFriendlyName': [\
                {'relatedStateVariable': 'GroupUUID', 'direction': 'in', 'name': 'GroupUUID'},\
                {'relatedStateVariable': 'GroupFriendlyName', 'direction': 'in', 'name': 'GroupFriendlyName'}],\
            'GetGroupMute': [\
                {'relatedStateVariable': 'GroupUUID', 'direction': 'in', 'name': 'GroupUUID'},\
                {'relatedStateVariable': 'GroupMute', 'direction': 'out', 'name': 'GroupMute'}],\
            'SetGroupBass': [\
                {'relatedStateVariable': 'GroupUUID', 'direction': 'in', 'name': 'GroupUUID'},\
                {'relatedStateVariable': 'GroupBass', 'direction': 'in', 'name': 'GroupBass'}],\
            'DestroyGroup': [\
                {'relatedStateVariable': 'GroupUUID', 'direction': 'in', 'name': 'GroupUUID'},\
                {'relatedStateVariable': 'PreserveZone', 'direction': 'in', 'name': 'PreserveZone'}],\
            'GetGroupUUID': [\
                {'relatedStateVariable': 'GroupUUID', 'direction': 'out', 'name': 'GroupUUID'}]}

        self._stateVarTbl={\
            'GroupBass': {'dataType': 'ui2', 'defaultValue': '0', 'allowedValueRange': {'step': '1', 'minimum': '0', 'maximum': '10'},\
                        'name': 'GroupBass', '@sendEvents': 'no'},\
            'GroupUpdating': {'dataType': 'boolean', 'defaultValue': '0', 'name': 'GroupUpdating', '@sendEvents': 'no'},\
            'A_ARG_TYPE_IPList': {'dataType': 'string', '@sendEvents': 'no', 'name': 'A_ARG_TYPE_IPList'},\
            'DeviceFriendlyName': {'dataType': 'string', '@sendEvents': 'no', 'name': 'DeviceFriendlyName'},\
            'CommandID': {'dataType': 'string', '@sendEvents': 'no', 'name': 'CommandID'},\
            'GroupMemberUUIDList': {'dataType': 'string', '@sendEvents': 'no', 'name': 'GroupMemberUUIDList'},\
            'AudioChannel': {'dataType': 'string', 'defaultValue': 'NORMAL', 'name':'AudioChannel', '@sendEvents': 'no', \
                        'allowedValueList': {'allowedValue': ['NORMAL', 'LEFT', 'RIGHT', 'REAR_LEFT', 'REAR_RIGHT', 'LOW_FREQUENCY', 'REAR_STEREO']}},\
            'GroupUUID': {'dataType': 'string', '@sendEvents': 'no', 'name': 'GroupUUID'},\
            'A_ARG_TYPE_CurrentState_GroupControl': {'dataType': 'string', '@sendEvents': 'no', 'name': 'A_ARG_TYPE_CurrentState_GroupControl'},\
            'PreserveZone': {'dataType': 'boolean', 'defaultValue': '0', 'name': 'PreserveZone', '@sendEvents': 'no'},\
            'GroupFriendlyName': {'dataType': 'string', '@sendEvents': 'no', 'name': 'GroupFriendlyName'},\
            'MediaServerUUID': {'dataType': 'string', '@sendEvents': 'no', 'name': 'MediaServerUUID'},\
            'A_ARG_TYPE_DummyValueGroupControl': {'dataType': 'string', '@sendEvents': 'no', 'name': 'A_ARG_TYPE_DummyValueGroupControl'},\
            'GroupVolume': {'dataType': 'ui2', 'defaultValue': '0', 'allowedValueRange': {'step': '1', 'minimum': '0', 'maximum': '100'},\
                        'name': 'GroupVolume', '@sendEvents': 'no'},\
            'ConfigDeviceUUID': {'dataType': 'string', '@sendEvents': 'no', 'name': 'ConfigDeviceUUID'},\
            'GroupMemberChannelList': {'dataType': 'string', '@sendEvents': 'no', 'name': 'GroupMemberChannelList'},\
            'GroupMute': {'dataType': 'boolean', 'defaultValue': '0', 'name': 'GroupMute', '@sendEvents': 'no'},\
            'ExtApSignalStrength': {'dataType': 'ui2', 'defaultValue': '0', 'allowedValueRange': {'step': '1', 'minimum': '0', 'maximum': '100'},\
                        'name': 'ExtApSignalStrength', '@sendEvents': 'no'},\
            'GroupBalance': {'dataType': 'ui2', 'defaultValue': '50', 'allowedValueRange': {'step': '1', 'minimum': '0', 'maximum': '100'},\
                        'name': 'GroupBalance', '@sendEvents': 'no'},\
            'GroupTreble': {'dataType': 'ui2', 'defaultValue': '0', 'allowedValueRange': {'step': '1', 'minimum': '0', 'maximum': '10'},\
                        'name': 'GroupTreble', '@sendEvents': 'no'},\
            'LastChange': {'dataType': 'string', '@sendEvents': 'yes', 'name': 'LastChange'},\
            'GroupStatus': {'dataType': 'string', 'defaultValue': 'NONE', 'name':'GroupStatus', '@sendEvents': 'no', \
                        'allowedValueList': {'allowedValue': ['LEADER', 'SLAVE', 'NONE']}}}

        self.xmlDict= {'scpd': {'actionList': {'action': [\
            {'argumentList': {'argument': [\
                {'relatedStateVariable': 'GroupUUID',\
                  'direction': 'in',\
                  'name': 'GroupUUID'},\
                {'relatedStateVariable': 'A_ARG_TYPE_IPList',\
                  'direction': 'in',\
                  'name': 'GroupMemberIPList'},\
                {'relatedStateVariable': 'GroupMemberUUIDList',\
                  'direction': 'in',\
                  'name': 'GroupMemberUUIDList'},\
                {'relatedStateVariable': 'GroupMemberChannelList',\
                  'direction': 'in',\
                  'name': 'GroupMemberChannelList'},\
                {'relatedStateVariable': 'GroupUUID',\
                  'direction': 'out',\
                  'name': 'GroupUUIDOut'}]},\
             'name': 'AddMembersToGroup'},\
            {'argumentList': {'argument': [\
                {'relatedStateVariable': 'GroupFriendlyName',\
                  'direction': 'in',\
                  'name': 'GroupFriendlyName'},\
                {'relatedStateVariable': 'GroupMemberUUIDList',\
                  'direction': 'in',\
                  'name': 'GroupMemberUUIDList'},\
                {'relatedStateVariable': 'GroupMemberChannelList',\
                  'direction': 'in',\
                  'name': 'GroupMemberChannelList'},\
                {'relatedStateVariable': 'GroupUUID',\
                  'direction': 'out',\
                  'name': 'GroupUUID'}]},\
             'name': 'CreateGroup'},\
            {'argumentList': {'argument': [\
                {'relatedStateVariable': 'GroupUUID',\
                  'direction': 'in',\
                  'name': 'GroupUUID'},\
                {'relatedStateVariable': 'PreserveZone',\
                  'direction': 'in',\
                  'name': 'PreserveZone'}]},\
             'name': 'DestroyGroup'},\
            {'argumentList': {'argument': [\
                {'relatedStateVariable': 'GroupUUID',\
                  'direction': 'in',\
                  'name': 'GroupUUID'},\
                {'relatedStateVariable': 'A_ARG_TYPE_DummyValueGroupControl',\
                  'direction': 'out',\
                  'name': 'DummyValue'}]},\
             'name': 'DummyAction_GroupControl'},\
            {'argumentList': {'argument': [\
                {'relatedStateVariable': 'GroupUUID',\
                  'direction': 'in',\
                  'name': 'GroupUUID'},\
                {'relatedStateVariable': 'ConfigDeviceUUID',\
                  'direction': 'out',\
                  'name': 'ConfigDeviceUUID'}]},\
             'name': 'GetConfigDeviceUUID'},\
            {'argumentList': {'argument': \
                {'relatedStateVariable': 'LastChange',\
                  'direction': 'out',\
                  'name': 'CurrentState'}},\
             'name': 'GetCurrentState'},\
            {'argumentList': {'argument': \
                {'relatedStateVariable': 'DeviceFriendlyName',\
                  'direction': 'out',\
                  'name': 'DeviceFriendlyName'}},\
                  'name': 'GetDeviceFriendlyName'},\
            {'argumentList': {'argument': [\
                {'relatedStateVariable': 'GroupUUID',\
                  'direction': 'in',\
                  'name': 'GroupUUID'},\
                {'relatedStateVariable': 'GroupBalance',\
                  'direction': 'out',\
                  'name': 'GroupBalance'}]},\
             'name': 'GetGroupBalance'},\
            {'argumentList': {'argument': [\
                {'relatedStateVariable': 'GroupUUID',\
                  'direction': 'in',\
                  'name': 'GroupUUID'},\
                {'relatedStateVariable': 'GroupBass',\
                  'direction': 'out',\
                  'name': 'GroupBass'}]},\
             'name': 'GetGroupBass'},\
            {'argumentList': {'argument': [\
                {'relatedStateVariable': 'GroupUUID',\
                  'direction': 'in',\
                  'name': 'GroupUUID'},\
                {'relatedStateVariable': 'GroupFriendlyName',\
                  'direction': 'out',\
                  'name': 'GroupFriendlyName'}]},\
             'name': 'GetGroupFriendlyName'},\
            {'argumentList': {'argument': [\
                {'relatedStateVariable': 'GroupUUID',\
                  'direction': 'in',\
                  'name': 'GroupUUID'},\
                {'relatedStateVariable': 'AudioChannel',\
                  'direction': 'out',\
                  'name': 'AudioChannel'}]},\
             'name': 'GetGroupMemberChannel'},\
            {'argumentList': {'argument': [\
                {'relatedStateVariable': 'GroupUUID',\
                  'direction': 'in',\
                  'name': 'GroupUUID'},\
                {'relatedStateVariable': 'GroupMemberUUIDList',\
                  'direction': 'out',\
                  'name': 'GroupMemberUUIDList'}]},\
             'name': 'GetGroupMemberList'},\
            {'argumentList': {'argument': [\
                {'relatedStateVariable': 'GroupUUID',\
                  'direction': 'in',\
                  'name': 'GroupUUID'},\
                {'relatedStateVariable': 'GroupMute',\
                  'direction': 'out',\
                  'name': 'GroupMute'}]},\
             'name': 'GetGroupMute'},\
            {'argumentList': {'argument': [\
                {'relatedStateVariable': 'GroupUUID',\
                  'direction': 'in',\
                  'name': 'GroupUUID'},\
                {'relatedStateVariable': 'GroupStatus',\
                  'direction': 'out',\
                  'name': 'GroupStatus'}]},\
             'name': 'GetGroupStatus'},\
            {'argumentList': {'argument': [\
                {'relatedStateVariable': 'GroupUUID',\
                  'direction': 'in',\
                  'name': 'GroupUUID'},\
                {'relatedStateVariable': 'GroupTreble',\
                  'direction': 'out',\
                  'name': 'GroupTreble'}]},\
             'name': 'GetGroupTreble'},\
            {'argumentList': {'argument': \
                {'relatedStateVariable': 'GroupUUID',\
                  'direction': 'out',\
                  'name': 'GroupUUID'}},\
             'name': 'GetGroupUUID'},\
            {'argumentList': {'argument': [\
                {'relatedStateVariable': 'GroupUUID',\
                  'direction': 'in',\
                  'name': 'GroupUUID'},\
                {'relatedStateVariable': 'GroupUpdating',\
                  'direction': 'out',\
                  'name': 'GroupUpdating'}]},\
             'name': 'GetGroupUpdating'},\
            {'argumentList': {'argument': [\
                {'relatedStateVariable': 'GroupUUID',\
                  'direction': 'in',\
                  'name': 'GroupUUID'},\
                {'relatedStateVariable': 'GroupVolume',\
                  'direction': 'out',\
                  'name': 'GroupVolume'}]},\
             'name': 'GetGroupVolume'},\
            {'argumentList': {'argument': [\
                {'relatedStateVariable': 'GroupUUID',\
                  'direction': 'in',\
                  'name': 'GroupUUID'},\
                {'relatedStateVariable': 'MediaServerUUID',\
                  'direction': 'out',\
                  'name': 'MediaServerUUID'}]},\
             'name': 'GetMediaServerUUID'},\
            {'argumentList': {'argument': [\
                {'relatedStateVariable': 'GroupUUID',\
                  'direction': 'in',\
                  'name': 'GroupUUID'},\
                {'relatedStateVariable': 'ExtApSignalStrength',\
                  'direction': 'out',\
                  'name': 'SignalStrength'}]},\
             'name': 'GetSignalStrength'},\
            {'argumentList': {'argument': [\
                {'relatedStateVariable': 'GroupUUID',\
                  'direction': 'in',\
                  'name': 'GroupUUID'},\
                {'relatedStateVariable': 'GroupMemberUUIDList',\
                  'direction': 'in',\
                  'name': 'GroupMemberUUIDList'}]},\
             'name': 'RemoveMembersFromGroup'},\
            {'argumentList': {'argument': \
                {'relatedStateVariable': 'DeviceFriendlyName',\
                  'direction': 'in',\
                  'name': 'DeviceFriendlyName'}},\
             'name': 'SetDeviceFriendlyName'},\
            {'argumentList': {'argument': [\
                {'relatedStateVariable': 'GroupUUID',\
                  'direction': 'in',\
                  'name': 'GroupUUID'},\
                {'relatedStateVariable': 'GroupBalance',\
                  'direction': 'in',\
                  'name': 'GroupBalance'},\
                {'relatedStateVariable': 'CommandID',\
                  'direction': 'in',\
                  'name': 'CommandID'}]},\
             'name': 'SetGroupBalance'},\
            {'argumentList': {'argument': [\
                {'relatedStateVariable': 'GroupUUID',\
                  'direction': 'in',\
                  'name': 'GroupUUID'},\
                {'relatedStateVariable': 'GroupBass',\
                  'direction': 'in',\
                  'name': 'GroupBass'}]},\
             'name': 'SetGroupBass'},\
            {'argumentList': {'argument': [\
                {'relatedStateVariable': 'GroupUUID',\
                  'direction': 'in',\
                  'name': 'GroupUUID'},\
                {'relatedStateVariable': 'GroupFriendlyName',\
                  'direction': 'in',\
                  'name': 'GroupFriendlyName'}]},\
             'name': 'SetGroupFriendlyName'},\
            {'argumentList': {'argument': [\
                {'relatedStateVariable': 'GroupUUID',\
                  'direction': 'in',\
                  'name': 'GroupUUID'},\
                {'relatedStateVariable': 'AudioChannel',\
                  'direction': 'in',\
                  'name': 'AudioChannel'}]},\
             'name': 'SetGroupMemberChannel'},\
            {'argumentList': {'argument': [\
                {'relatedStateVariable': 'GroupUUID',\
                  'direction': 'in',\
                  'name': 'GroupUUID'},\
                {'relatedStateVariable': 'GroupMute',\
                  'direction': 'in',\
                  'name': 'GroupMute'},\
                {'relatedStateVariable': 'CommandID',\
                  'direction': 'in',\
                  'name': 'CommandID'}]},\
             'name': 'SetGroupMute'},\
            {'argumentList': {'argument': [\
                {'relatedStateVariable': 'GroupUUID',\
                  'direction': 'in',\
                  'name': 'GroupUUID'},\
                {'relatedStateVariable': 'GroupTreble',\
                  'direction': 'in',\
                  'name': 'GroupTreble'}]},\
             'name': 'SetGroupTreble'},\
            {'argumentList': {'argument': [\
                {'relatedStateVariable': 'GroupUUID',\
                  'direction': 'in',\
                  'name': 'GroupUUID'},\
                {'relatedStateVariable': 'GroupVolume',\
                  'direction': 'in',\
                  'name': 'GroupVolume'},\
                {'relatedStateVariable': 'CommandID',\
                  'direction': 'in',\
                  'name': 'CommandID'}]},\
             'name': 'SetGroupVolume'}]},\
            'serviceStateTable': {'stateVariable': [\
                {'dataType': 'string',\
                  '@sendEvents': 'no',\
                  'name': 'A_ARG_TYPE_CurrentState_GroupControl'},\
                {'dataType': 'string',\
                  '@sendEvents': 'no',\
                  'name': 'A_ARG_TYPE_DummyValueGroupControl'},\
                {'dataType': 'string',\
                  '@sendEvents': 'no',\
                  'name': 'A_ARG_TYPE_IPList'},\
                {'dataType': 'string',\
                  'defaultValue': 'NORMAL',\
                  'name': 'AudioChannel',\
                  '@sendEvents': 'no',\
                  'allowedValueList': {'allowedValue': [\
                      'NORMAL',\
                      'LEFT',\
                      'RIGHT',\
                      'REAR_LEFT',\
                      'REAR_RIGHT',\
                      'LOW_FREQUENCY',\
                      'REAR_STEREO']}},\
                {'dataType': 'string',\
                  '@sendEvents': 'no',\
                  'name': 'CommandID'},\
                {'dataType': 'string',\
                  '@sendEvents': 'no',\
                  'name': 'ConfigDeviceUUID'},\
                {'dataType': 'string',\
                  '@sendEvents': 'no',\
                  'name': 'DeviceFriendlyName'},\
                {'dataType': 'ui2',\
                  'defaultValue': '0',\
                  'allowedValueRange': \
                     {'step': '1',\
                      'minimum': '0',\
                      'maximum': '100'},\
                      'name': 'ExtApSignalStrength',\
                      '@sendEvents': 'no'},\
                {'dataType': 'ui2',\
                  'defaultValue': '50',\
                  'allowedValueRange': \
                     {'step': '1',\
                      'minimum': '0',\
                      'maximum': '100'},\
                      'name': 'GroupBalance',\
                      '@sendEvents': 'no'},\
                {'dataType': 'ui2',\
                  'defaultValue': '0',\
                  'allowedValueRange': \
                     {'step': '1',\
                      'minimum': '0',\
                      'maximum': '10'},\
                      'name': 'GroupBass',\
                      '@sendEvents': 'no'},\
                {'dataType': 'string',\
                  '@sendEvents': 'no',\
                  'name': 'GroupFriendlyName'},\
                {'dataType': 'string',\
                  '@sendEvents': 'no',\
                  'name': 'GroupMemberChannelList'},\
                {'dataType': 'string',\
                  '@sendEvents': 'no',\
                  'name': 'GroupMemberUUIDList'},\
                {'dataType': 'boolean',\
                  'defaultValue': '0',\
                  'name': 'GroupMute',\
                  '@sendEvents': 'no'},\
                {'dataType': 'string',\
                  'defaultValue': 'NONE',\
                  'name': 'GroupStatus',\
                  '@sendEvents': 'no',\
                  'allowedValueList': {\
                      'allowedValue': [\
                      'LEADER',\
                      'SLAVE',\
                      'NONE']}},\
                {'dataType': 'ui2',\
                  'defaultValue': '0',\
                  'allowedValueRange': \
                      {'step': '1',\
                       'minimum': '0',\
                       'maximum': '10'},\
                  'name': 'GroupTreble',\
                  '@sendEvents': 'no'},\
                {'dataType': 'string',\
                  '@sendEvents': 'no',\
                  'name': 'GroupUUID'},\
                {'dataType': 'boolean',\
                  'defaultValue': '0',\
                  'name': 'GroupUpdating',\
                  '@sendEvents': 'no'},\
                {'dataType': 'ui2',\
                  'defaultValue': '0',\
                  'allowedValueRange': \
                     {'step': '1',\
                      'minimum': '0',\
                      'maximum': '100'},\
                      'name': 'GroupVolume',\
                      '@sendEvents': 'no'},\
                {'dataType': 'string',\
                  '@sendEvents': 'yes',\
                  'name': 'LastChange'},\
                {'dataType': 'string',\
                  '@sendEvents': 'no',\
                  'name': 'MediaServerUUID'},\
                {'dataType': 'boolean',\
                  'defaultValue': '0',\
                  'name': 'PreserveZone',\
                  '@sendEvents': 'no'}]},\
                  'specVersion': {'major': '1',\
                  'minor': '0'}}}

        self.cmndList=\
                ['AddMembersToGroup',\
                 'CreateGroup',\
                 'DestroyGroup',\
                 'DummyAction_GroupControl',\
                 'GetConfigDeviceUUID',\
                 'GetCurrentState',\
                 'GetDeviceFriendlyName',\
                 'GetGroupBalance',\
                 'GetGroupBass',\
                 'GetGroupFriendlyName',\
                 'GetGroupMemberChannel',\
                 'GetGroupMemberList',\
                 'GetGroupMute',\
                 'GetGroupStatus',\
                 'GetGroupTreble',\
                 'GetGroupUUID',\
                 'GetGroupUpdating',\
                 'GetGroupVolume',\
                 'GetMediaServerUUID',\
                 'GetSignalStrength',\
                 'RemoveMembersFromGroup',\
                 'SetDeviceFriendlyName',\
                 'SetGroupBalance',\
                 'SetGroupBass',\
                 'SetGroupFriendlyName',\
                 'SetGroupMemberChannel',\
                 'SetGroupMute',\
                 'SetGroupTreble',\
                 'SetGroupVolume']
        return