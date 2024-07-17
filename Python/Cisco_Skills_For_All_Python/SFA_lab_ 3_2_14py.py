# Lab 3.2.14 - Building a Pyramid
# Author: Fredric Gluck
# Date: 10 May 2023
# -----------------------------------
# Your task is to write a program which reads the
# number of blocks the builders have, and
# outputs the height of the pyramid that can be built
# using these blocks.
#
# Note: the height is measured by the number of fully
# completed layers – if the builders don't have a
# sufficient number of blocks and cannot
# complete the next layer, they
# finish their work immediately.
# Extra Challange: Print a picture of the pyramid stack
#
# Set the number of the current level to 1
currentBlocksRequired = 1
layersCompleted = 0
blocksUsed = 0
# Input the number of blocks
totalBlocks = int(input("How many blocks do you have? >>> "))
blocksMessage = "You started with " + str(totalBlocks) + " blocks."
# Test the number of remaining blocks to see if you can do
while totalBlocks >= currentBlocksRequired:
    print(currentBlocksRequired*"*")  # print the current layer
    blocksUsed = blocksUsed + currentBlocksRequired
    # You used up blocks for the layer
    totalBlocks = totalBlocks - currentBlocksRequired
    currentBlocksRequired += 1  # Prepare for the next layer
    layersCompleted += 1  # Keeps track of the number of layers completed
print(f"All done.")
print(blocksMessage)
print(f"The pyramid is {layersCompleted} layers high. ")
print(f"You used {blocksUsed} blocks.")
if totalBlocks != 0:
    print(f"The next layer needed {currentBlocksRequired} blocks.")
    print(f"You had {totalBlocks} blocks left over.")
else:
    print("You have no blocks left over!")
