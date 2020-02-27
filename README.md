# About #

SHOE - An open source HEOS configuration and control project written in python 3.7.

SHOE is designed first as a configuration tool for HEOS devices.  It uses XML HTTP commands, like those in the HEOS App, and it is designed to replace and possibly extend the functionality of the app.  SHOE has been developed and tested on HEOS1 HS2 speakers, running version 1.520.200 firmware.

The SHOE package is split into two components:
1. A library call **shoelib** that enables access to HEOS speakers via other Python programs. This
   provides the low level communication interface.
2. A CLI client program called **shoe** that provides a front end to drive **shoelib**
   functionality.

Currently, **shoe** has no special commands to use the speakers as renderers or control the speakers as streaming devices.  However, it does expose the renderer device command.  This functionality can be achieved using a variety of uPNP software packages.

Note that SHOE is *not* based on the HEOS CLI interface published by Denon.  That interface has limited functionality with regards to configuration.  For instance, the CLI spec doesn't address the creations of "Zones" and does not display Groups generated by the app.  The CLI may be useful for implementing playback functions, if SHOE ever goes that way, but the XML HTTP appears to expose a far more feature rich set.

## Licensing and Stuff ##
SHOE provided free, "as is", without warranty, under the GPL3 License.  Please read "LICENSE" file for details.  Use at your own risk.
Copyright (C) 2020

# Using SHOE #
## Install ##
To install:
Use PIP -

    python3 -m pip install shoe

Or from git, clone from -

    https://github.com/mkarasoff/shoe

##Other Requirements##
Python 3
python-lxml library

Shoe does not yet implement SSDP discovery, so one must know the IP address.

## Speaker Network Setup ##
To setup a HEOS speaker for the network without the HEOS App:

    http://<Speaker IP>/settings/index.html

To update the speaker or disable automatic firmware updates without the HEOS App:

    http://<Speaker IP>/settings/upgrade.html

## Running ##
A quick check of operation can tested here:

    shoe -H <Speaker IP> -i

This should return something like:

    Info for <Speaker IP>
    ----------------
    friendlyName     : <SPEAKER NAME>
    manufacturer     : Denon
    manufacturerURL  : http://www.denon.com
    modelName        : HEOS 1
    modelNumber      : DWS-1000 4.0
    serialNumber     : ACJG00000000
    UDN              : uuid:00000000-0000-0000-0000-000000000000
    DeviceID         : AIOS:0001
    firmwareRevision : 147202
    firmware_date    : Thu 2019-09-12 02:43:50
    firmware_version : 1.520.200
    lanMac           : 00:00:00:00:00:00
    locale           : en_NA
    moduleRevision   : 4
    moduleType       : Aios 4.0
    productRevision  : 3
    releaseType      : Production
    wlanMac          : 00:00:00:00:00:00

To get additional information:

    shoe -H <Speaker IP> -ii
or

    shoe -H <Speaker IP> -iii

To set a name:

    shoe -H <Speaker IP> -n <Speaker Name>

To combine speakers into a stereo pair:

    shoe -H <Lead Speaker IP> <Other Speaker IP> -b <Bond Name>

The `<Bond Name>` will appear in your DLNA/uPNP client as a renderer.

## CLI ##

    usage: shoe [-h] [-q] [-v] -H HOSTS [HOSTS ...] [-i] [-t] [-n <Speaker Name>]
                [-u] [-b <Bond Name>] [-s] [-f] [-D <Device Name>]
                [-F <Root File Name>] [-S <Service Name>] [-x <Root URL Path>]
                [-c <Command>] [-a <Name> <Value>] [-p <Command> [<Command> ...]]

    optional arguments:
      -h, --help            show this help message and exit
      -q, --quiet           make output quiet
      -v, --verbose         Increase output verbosity. '-vv' and '-vvv' will show
                            more.
      -H HOSTS [HOSTS ...], --Host HOSTS [HOSTS ...]
                            This will set the host for the operation, usually an
                            IP address. At least one host is required. For some
                            operations (e.g. -b) multiple hosts can be given. If
                            only one host is required for the command, then the
                            first host will be used. Port can be specified with
                            ':' as in '<host>:<port>'
      -i, --info            Displays info for devices. '-ii' and '-iii' will show
                            more
      -t, --tree            Displays Command Tree. Defaults to showing commands
                            from AIOS, Group, and Zone services. Add a second t,
                            '-tt' to show commands from all services.
      -n <Speaker Name>, --name <Speaker Name>
                            This will name a speaker. If multiple hosts are given,
                            multiple names may also be given. Names will be
                            assigned in order ofhosts given by the (-H) command
      -u, --unBond          This will delete the bond
      -b <Bond Name>, --bond <Bond Name>
                            This will bond all hosts given on command line with
                            the (-H) command, making a multichannel speaker
                            grouping with the name <Bond Name>. The channel
                            assignment will be based on the order of hosts given
                            by the (-H) command: Left, Right, RearL, RearR,
                            Center, Sub. If two speakers are given, the pair will
                            be stereo, and surround speakers will be added for
                            more than two speakers. Speaker channels can be
                            modified with the (-s) command.
      -s, --swap            Swaps left and right speakers
      -f, --force           Send commmand without parameter checks. Requires '-D'
                            and '-S' options to work correctly
      -D <Device Name>, --device <Device Name>
                            Select a device.
      -F <Root File Name>, --rootFileName <Root File Name>
                            Use file given by <Root File Name> for the root
                            configuration, rather than URL.
      -S <Service Name>, --service <Service Name>
                            Select a service.
      -x <Root URL Path>, --rootUrlPath <Root URL Path>
                            Specifies a URL for the root XML configuration file.
                            By default, this is the config path is
                            "/upnp/desc/aios_device/aios_device.xml", for HEOS1
                            running firmware version 1.520.200
      -c <Command>, --cmnd <Command>
                            Select a command. The command can be followed by (-a)
                            to give arguments for the command. If multiple hosts
                            are given with the (-H) option, the command will be
                            run on all hosts. If device and service are not
                            specified with (-d) and (-s) options, and the command
                            name is duplicated across services, it will be run on
                            all matching services.
      -a <Name> <Value>, --arg <Name> <Value>
                            Set an argument given to an expert command (-e). Must
                            give two values: <Name> indicates the name of the
                            argument. <Value> indicates the value of the argument.
                            For commands that require multiple arguments, use more
                            (-a). If all required arguments are given, with -e,
                            the command will run.
      -p <Command> [<Command> ...], --param <Command> [<Command> ...]
                            List command argument parameters. Returns hints for
                            argument parameters for the command given by (-c).

## Extended Commands ##
SHOE provides access to extended commands not directly accessible using the HEOS app.  In a way, these commands are "hidden".  There is no documentation on how they work, nor directly accessible or documented in the HEOS app.

These commands are broken down into a hierarchy of "devices" and "services" that run on the speaker.  These commands are organized into a "command tree":

    Device
        |
        |\_Service
        |     |
    Device     \_Commands
        |
        |\_Service
        |     |
        |      \_Commands
        |
         \_Service
              |
            .  \_Commands
            .
            .
           etc.

SHOE will show the device command tree with the `-t` option:

    shoe -H <Speaker IP> -t[t]

This would return a list of commands:

    $ shoe -H <Speaker IP> -tt

    Device: ACT-Denon :
        Service: ACT     :
        ----------------
                               AddNetworkShare
                               ApplyChanges
                               CancelChanges
                               CancelFirmwareUpgrade
                               CheckForFirmwareUpgrade
                               DeleteNetworkShare
                               GetAccessPointList
                               GetActiveInterface
                               GetAudioConfig
                               GetBluetoothStatus
                               GetConfigurationStatus
                               GetConfigurationToken
                               GetCurrentLanguage
                               GetCurrentState
                               GetDaylightSaving
                               GetFriendlyName
                               GetHEOSNetID
                               GetLEDConfig
                               GetNetworkConfiguration
                               GetNetworkConfigurationList
                               GetNetworkShares
                               GetP2PMode
                               GetSessionId
                               GetSupportedLanguageList
                               GetSurroundSpeakerConfig
                               GetTimeZone
                               GetTranscode
                               GetUpdateAction
                               GetUpdateLevel
                               GetUpgradeProgress
                               GetUpgradeStatus
                               GetVolumeLimit
                               GetWirelessProfile
                               GetWirelessState
                               GetWirelessStatus
                               ReIndexNetworkShare
                               ReMountNetworkShare
                               RegisterUser
                               ReleaseConfigurationToken
                               SetAudioConfig
                               SetBluetoothAction
                               SetConfigurationStatus
                               SetCurrentLanguage
                               SetDaylightSaving
                               SetFriendlyName
                               SetHEOSNetID
                               SetLEDConfig
                               SetNetworkConfiguration
                               SetSessionId
                               SetSurroundSpeakerConfig
                               SetTimeZone
                               SetTranscode
                               SetUpdateAction
                               SetUpdateLevel
                               SetVolumeLimit
                               SetWPSPinSSID
                               SetWirelessProfile
                               StartInvitation
                               StartWifiAp
                               StopInvitation
                               StopWifiAp
                               SubmitDiagnostics
                               UpdateFirmware
        ----------------
    Device: AiosServices :
        Service: ErrorHandler :
        ----------------
                               ClearError
                               DummyAction_ErrorHandler
        ----------------
        Service: ZoneControl :
        ----------------
                               AddMemberToZone
                               CreateZone
                               DestroyZone
                               DummyAction_ZoneControl
                               GetCurrentState
                               GetMemberStatus
                               GetZoneConnectedList
                               GetZoneFriendlyName
                               GetZoneMemberList
                               GetZoneMinimise
                               GetZoneMute
                               GetZoneStatus
                               GetZoneUUID
                               GetZoneVolume
                               RemoveMemberFromZone
                               SetZoneFriendlyName
                               SetZoneMinimise
                               SetZoneMute
                               SetZoneVolume
                               TestZoneConnectivity
        ----------------
        Service: GroupControl :
        ----------------
                               AddMembersToGroup
                               CreateGroup
                               DestroyGroup
                               DummyAction_GroupControl
                               GetConfigDeviceUUID
                               GetCurrentState
                               GetDeviceFriendlyName
                               GetGroupBalance
                               GetGroupBass
                               GetGroupFriendlyName
                               GetGroupMemberChannel
                               GetGroupMemberList
                               GetGroupMute
                               GetGroupStatus
                               GetGroupTreble
                               GetGroupUUID
                               GetGroupUpdating
                               GetGroupVolume
                               GetMediaServerUUID
                               GetSignalStrength
                               RemoveMembersFromGroup
                               SetDeviceFriendlyName
                               SetGroupBalance
                               SetGroupBass
                               SetGroupFriendlyName
                               SetGroupMemberChannel
                               SetGroupMute
                               SetGroupTreble
                               SetGroupVolume
        ----------------
        ----------------
    Device: MediaRenderer :
        Service: AVTransport :
        ----------------
                               GetCurrentState
                               GetCurrentTransportActions
                               GetDeviceCapabilities
                               GetMediaInfo
                               GetMediaInfo_Ext
                               GetPositionInfo
                               GetTransportInfo
                               GetTransportSettings
                               Next
                               Pause
                               Play
                               Previous
                               Seek
                               SetAVTransportURI
                               SetNextAVTransportURI
                               SetPlayMode
                               Stop
                               X_SetShuffle
        ----------------
        Service: ConnectionManager :
        ----------------
                               ConnectionComplete
                               GetCurrentConnectionIDs
                               GetCurrentConnectionInfo
                               GetCurrentState
                               GetProtocolInfo
                               PrepareForConnection
        ----------------
        Service: RenderingControl :
        ----------------
                               GetCurrentState
                               GetMute
                               GetVolume
                               GetVolumeDB
                               ListPresets
                               SelectPreset
                               SetMute
                               SetVolume
                               SetVolumeDB
                               X_GetBalance
                               X_GetBass
                               X_GetPreset
                               X_GetSubwoofer
                               X_GetTreble
                               X_SetBalance
                               X_SetBass
                               X_SetMute
                               X_SetSubwoofer
                               X_SetTreble
                               X_SetVolume
        ----------------
    Device: MediaServer :
        Service: ContentDirectory :
        ----------------
                               Browse
                               GetSearchCapabilities
                               GetSortCapabilities
                               GetSystemUpdateID
                               Search
                               X_HideItem
                               X_RenameItem
                               X_SetItemInputLevel
        ----------------
        Service: ConnectionManager :
        ----------------
                               ConnectionComplete
                               GetCurrentConnectionIDs
                               GetCurrentConnectionInfo
                               GetCurrentState
                               GetProtocolInfo
                               PrepareForConnection
        ----------------

Argument for any of these commands can be found:

    $ shoe -H <Speaker IP> -p <Command Name>

For Example:

    $ shoe -H <Speaker IP> -p GetGroupBalance

    Cmnd:    GetGroupBalance
    Device:  AiosServices
    Service: GroupControl
    Parameters       :
    ----------------
        name             : GroupUUID
        direction        : in
        state            :
            dataType         : string
            @sendEvents      : no
    ----------------
        name             : GroupBalance
        direction        : out
        state            :
            dataType         : ui2
            defaultValue     : 50
            allowedValueRange :
                minimum          : 0
                maximum          : 100
                step             : 1
            @sendEvents      : no
    ----------------

This indicates that GroupUUID is required as an input parameter, and GroupBalance is an output.  To get the group balance, one must first get the GroupUUID:

    $ shoe -H <Speaker IP> -c GetGroupUUID

    Cmnd: GetGroupUUIDResponse   Service: GroupControl   Device: AiosServices
    GroupUUID        : 00000000000000000000000000000000

    $ shoe -H <Speaker IP> -c GetGroupBalance -a GroupUUID 00000000000000000000000000000000

    Cmnd: GetGroupBalanceResponse   Service: GroupControl   Device: AiosServices
    GroupBalance     : 50

## Other Version of Hardware ##
Other version of hardware and firmware may work with SHOE.  SHOE requires a root XML, served from the HEOS device, to configure itself.  The URL can be found in the payload header of SSDP packets, gathered using a packet sniffing tool such as wireshark:

    LOCATION: http://<Speaker IP>:<Port>/upnp/desc/aios_device/aios_device.xml

This is the location of the root XML file for the HEOS 1 speaker, version 1.520.200.  Other devices may have a different location.  The `shoe` program allows one to specify URL or a file on the command line.

## Security considerations ##
Just like the HEOS app, all communication between SHOE and Denon HEOS speakers is plaintext, without password protection.  From a practical perspective, any sensitive information stored on you speakers, including your WIFI password, may be be gathered through trivial methods.  Anyone with network access to your speaker, either via WIFI, or physical access to the Ethernet port, can access and control you speakers with SHOE.  Consider this when setting up your speakers on your network.

# Version Release Notes #

## v(0.1.5) ##

The goal is to remove configuration dependence from the HEOS app. SHOE will provide a minimal CLI interface that address devices via IP and allow for configuration of speakers without the use of the HEOS app.  With the limited feature set, the test focus will primarily be on ACT, GroupConfig, and ZoneConfig services.

The following features are implemented:
1. Display information from the HEOS device.
2. Provide CLI interface to execute individual commands on the HEOS device in an "Expert Mode'
3. Script more complex actions for easy configuration:
- Naming a device
- Binding devices into a "Zone" for multichannel speaker operation
- Selecting channels.

## v(0.1.7) ##
- Fixed some issues with alternate xml url (-x option).
- Added versioning option.
- Better response if no host is given.
- Fixed bug with shoeBond.

## v(0.1.9) ##
- Set python minimum version for PIP install to >=3.6
- Added extended commands to README.md
- Typo fixes to README.md

# Future Possibilities #

Possible future features:
- Discovery
- Network configuration
- Bluetooth configuration
- LED intensity
- Rendering w/ streaming services
