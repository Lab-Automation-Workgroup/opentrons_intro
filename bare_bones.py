# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

To do 


"""

from opentrons import protocol_api


# metadata
metadata = {
    'protocolName': 'Learn about opentrons',
    'author': 'Name vikmol@dtu.dk',
    'description': 'This is for learning opentrons',
    'apiLevel': '2.4'
}

# protocol run function. the part after the colon lets your editor know
# where to look for autocomplete suggestions
def run(protocol: protocol_api.ProtocolContext):

    """ load labware """
    my_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '11')
    my_tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '6')
    

    """ Variables"""
    # numSamps is the number of samples and should be 1-96 (int)

    """ load pipettes """
    p300 = protocol.load_instrument('p300_single', 'right', tip_racks=[my_tiprack])

    """ helper functions """
    # def my_helper_fxn():
    #     protocol.comment('I am helping!')

    """ liquid transfer commands """
    # p300.transfer(100, my_plate.wells()[0], my_plate.wells()[1])
    # p300.transfer(100, my_plate['A1'], my_plate['B2'])
    
    p300.pick_up_tip()
    p300.aspirate(100, my_plate['A1'])
    p300.dispense(100, my_plate['B1'])
    p300.drop_tip()

    for well in my_plate.wells():
        print(well)
    # print(my_plate.columns()[0][0])



if __name__ == '__main__':
    from opentrons.simulate import get_protocol_api
    # from opentrons.simulate import format_runlog
    # import opentrons
    
    # load the protocol name
    protocol = get_protocol_api('2.11')
    # load your run function with the OT commands
    run(protocol)
    # print out the OT commands
    for line in protocol.commands():
        print(line)