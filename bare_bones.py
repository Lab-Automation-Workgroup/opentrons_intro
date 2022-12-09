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

# change in file 

# protocol run function. the part after the colon lets your editor know
# where to look for autocomplete suggestions
def run(protocol: protocol_api.ProtocolContext):

    """ load labware """
    pcr_plate = protocol.load_labware('biorad_96_wellplate_200ul_pcr', '6')
    MTP = protocol.load_labware('nest_96_wellplate_200ul_flat', '9')
    my_tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '11')
    

    """ Variables"""
    # numSamps is the number of samples and should be 1-96 (int)
    NUMBER_OF_ROWS = 1

    """ load pipettes """
    p300 = protocol.load_instrument('p300_multi', 'right', tip_racks=[my_tiprack])

    """ helper functions """
    # def my_helper_fxn():
    #     protocol.comment('I am helping!')
    def transfer_simple(volume, source_row, destination_row):
        p300.flow_rate.aspirate = 120
        p300.mix(volume, 3, source_row)
        p300.aspirate(volume, source_row.bottom(1))
        p300.dispense(volume, destination_row.bottom(5))
        p300.blow_out()


    """ liquid transfer commands """
    for i in range(NUMBER_OF_ROWS):
        p300.pick_up_tip()
        transfer_simple(100, MTP.rows()[0][i], pcr_plate.rows()[0][i])
        p300.drop_tip()
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