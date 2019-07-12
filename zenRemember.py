"""
Jason Mitchell

Simple script that saves an objects positioning and saves a button to the shelf.  Effective Uses:
    -Save poses
    -Will update UI at a later date to use for different light setups/save capability


SETUP

First things first:

1. Place Icons in Maya's icons folder.  If you uncomment and run line 44, your preferences directory will be listed.
   You should paste the icons inside the icons folder(Do Not Rename them, if you do, you will have to update the code with the new names).
   Make sure to comment the line out again once you're done.

Editing Saved Poses

2. Poses will be saved to their perspective tabs within the tool, however you can also drage the pose you want to edit to your Maya shelves.
   Once a pose is created and a button appears in a pose tab, right click>edit.  You will be able to edit the attributes of the pose.

How to Run: Two Options

1. Copy and paste the code into a Python tab in your Script Editor.  Then run.

2. Copy and paste the python script to your scripts folder (refer to line 45 if you need the directory).
   Copy and paste the following in the Script Editor, then run:  (Make sure to have the icons in your icons folder, if not,
   default icons will appear)

import zenRemember
reload(zenRemember)


How to Use:

While posing an object, character, etc...clcik an icon that matches the area you're posing.  For example:
Posing the entire body of a character, click the body icon, and all of the controls' attributes will be saved.
You can then click on the "Body" tab to refer back to that pose.

"""
import pymel.core as pm


#print pm.internalVar(upd = True)
#pm.internalVar(usd = True)

if pm.window("zenWindow", q = True, ex = True):
    pm.deleteUI("zenWindow", window = True)


#Create title and UI dimensions
pm.window("zenWindow", t = "Zen Remember", resizeToFitChildren = True, s = True)


zForm = pm.formLayout()
zTabs = pm.tabLayout()

pm.formLayout(zForm, edit = True, attachForm = [(zTabs, "top", 5), (zTabs, "bottom", 5), (zTabs, "left", 5), (zTabs, "right", 5)])


crtPose_layout = pm.columnLayout()
poseShelf = pm.shelfLayout(w = 400, h = 550)


#Images must have exact naming convention as they show in icons folder
crtPose_body = pm.symbolButton(image = "zenRemember_bodyIcon.png", w = 150, h = 150, c = "saveToTab_body(bodyShelf)")
crtPose_facial = pm.symbolButton(image = "zenRemember_faceIcon.png", w = 150, h = 150, c = "saveToTab_face(faceShelf)")
crtPose_arm = pm.symbolButton(image = "zenRemember_armsIcon.png", w = 150, h = 150, c = "saveToTab_arm(armShelf)")
crtPose_hands = pm.symbolButton(image = "zenRemember_handIcon.png", w = 150, h = 150, c = "saveToTab_hand(handShelf)")
crtPose_legs = pm.symbolButton(image = "zenRemember_legsIcon.png", w = 150, h = 150, c = "saveToTab_leg(legShelf)")
crtPose_feet = pm.symbolButton(image = "zenRemember_feetIcon.png", w = 150, h = 150, c = "saveToTab_feet(feetShelf)")

#Create seperate tabs layout
pm.setParent("..")

pm.setParent("..")

bodyPose_layout = pm.columnLayout()

bodyShelf = pm.shelfLayout(w = 500, h = 500)


pm.setParent("..")

pm.setParent("..")

facePose_layout = pm.columnLayout()

faceShelf = pm.shelfLayout(w = 500, h = 500)


pm.setParent("..")

pm.setParent("..")

armPose_layout = pm.columnLayout()

armShelf = pm.shelfLayout(w = 500, h = 500)


pm.setParent("..")

pm.setParent("..")

handPose_layout = pm.columnLayout()

handShelf = pm.shelfLayout(w = 500, h = 500)


pm.setParent("..")

pm.setParent("..")

legPose_layout = pm.columnLayout()

legShelf = pm.shelfLayout(w = 500, h = 500)


pm.setParent("..")

pm.setParent("..")

feetPose_layout = pm.columnLayout()

feetShelf = pm.shelfLayout(w = 500, h = 500)


pm.setParent("..")

pm.setParent("..")
pm.tabLayout(zTabs, edit = True, tabLabel = [(crtPose_layout, "Pose Categories"), (bodyPose_layout, "Body"), (facePose_layout, "Face"), (armPose_layout, "Arm"), (handPose_layout, "Hand"), (legPose_layout, "Leg"), (feetPose_layout, "Feet")])



pm.showWindow("zenWindow")


def saveToTab_body(target_bodyShelf):
    #Clear out old data to store clean new data
    storeCmds_body = ""

    #List selected
    selPose = pm.ls(sl = True)

    #Error window if nothing selected
    #List keyable, readable, writable, connectable, and unlocked attributes in selected
    #Grab values of selected and concatenates keyable channels
    if len(selPose) < 1:
        pm.warning("Nothing Selected.  Please select at least one object.")
    else:
        for all in selPose:
            keyable = pm.listAttr(all, k = True, r = True, w = True, c = True, u = True)
            print keyable
            for vals in keyable:
                findVal = pm.getAttr(all + "." + vals)
                print findVal
                starterCiph = "setAttr "
                enderCiph = ";\n"
                shelfSave = (starterCiph + (all + "." + vals) + " %f" + enderCiph) % findVal
                storeCmds_body += shelfSave
                print storeCmds_body

        #prompt dialog for artist to enter a name of the pose and button to save to shelf
        pd_body = pm.promptDialog(t = "Body Pose", m = "Name of Pose?", b = "Save to Shelf")


        if pd_body == "Save to Shelf":

            pd_body_name = pm.promptDialog(q = True, text = True)
            #pm.internalVar(usd = True)
            pm.shelfButton(l = pd_body_name, ann = pd_body_name, imageOverlayLabel = pd_body_name, i1 = "zenRemember_bodyIcon.png", command = storeCmds_body, p = target_bodyShelf, sourceType = "mel")


def saveToTab_face(target_faceShelf):
    #Clear out old data to store clean new data
    storeCmds_face = ""

    #List selected
    selPose = pm.ls(sl = True)

    #Error window if nothing selected
    #List keyable, readable, writable, connectable, and unlocked attributes in selected
    #Grab values of selected and concatenates keyable channels
    if len(selPose) < 1:
        pm.warning("Nothing Selected.  Please select at least one object.")
    else:
        for all in selPose:
            keyable = pm.listAttr(all, k = True, r = True, w = True, c = True, u = True)
            print keyable
            for vals in keyable:
                findVal = pm.getAttr(all + "." + vals)
                print findVal
                starterCiph = "setAttr "
                enderCiph = ";\n"
                shelfSave = (starterCiph + (all + "." + vals) + " %f" + enderCiph) % findVal
                storeCmds_face += shelfSave
                print storeCmds_face

        #prompt dialog for artist to enter a name of the pose and button to save to shelf
        pd_face = pm.promptDialog(t = "Face Pose", m = "Name of Pose?", b = "Save to Shelf")


        if pd_face == "Save to Shelf":

            pd_face_name = pm.promptDialog(q = True, text = True)
            #pm.internalVar(usd = True)
            pm.shelfButton(l = pd_face_name, ann = pd_face_name, imageOverlayLabel = pd_face_name, i1 = "zenRemember_faceIcon.png", command = storeCmds_face, p = target_faceShelf, sourceType = "mel")



def saveToTab_arm(target_armShelf):
    #Clear out old data to store clean new data
    storeCmds_arm = ""

    #List selected
    selPose = pm.ls(sl = True)

    #Error window if nothing selected
    #List keyable, readable, writable, connectable, and unlocked attributes in selected
    #Grab values of selected and concatenates keyable channels
    if len(selPose) < 1:
        pm.warning("Nothing Selected.  Please select at least one object.")
    else:
        for all in selPose:
            keyable = pm.listAttr(all, k = True, r = True, w = True, c = True, u = True)
            print keyable
            for vals in keyable:
                findVal = pm.getAttr(all + "." + vals)
                print findVal
                starterCiph = "setAttr "
                enderCiph = ";\n"
                shelfSave = (starterCiph + (all + "." + vals) + " %f" + enderCiph) % findVal
                storeCmds_arm += shelfSave
                print storeCmds_arm

        #prompt dialog for artist to enter a name of the pose and button to save to shelf
        pd_arm = pm.promptDialog(t = "Arm Pose", m = "Name of Pose?", b = "Save to Shelf")


        if pd_arm == "Save to Shelf":

            pd_arm_name = pm.promptDialog(q = True, text = True)
            #pm.internalVar(usd = True)
            pm.shelfButton(l = pd_arm_name, ann = pd_arm_name, imageOverlayLabel = pd_arm_name, i1 = "zenRemember_armsIcon.png", command = storeCmds_arm, p = target_armShelf, sourceType = "mel")



def saveToTab_hand(target_handShelf):
    #Clear out old data to store clean new data
    storeCmds_hand = ""

    #List selected
    selPose = pm.ls(sl = True)

    #Error window if nothing selected
    #List keyable, readable, writable, connectable, and unlocked attributes in selected
    #Grab values of selected and concatenates keyable channels
    if len(selPose) < 1:
        pm.warning("Nothing Selected.  Please select at least one object.")
    else:
        for all in selPose:
            keyable = pm.listAttr(all, k = True, r = True, w = True, c = True, u = True)
            print keyable
            for vals in keyable:
                findVal = pm.getAttr(all + "." + vals)
                print findVal
                starterCiph = "setAttr "
                enderCiph = ";\n"
                shelfSave = (starterCiph + (all + "." + vals) + " %f" + enderCiph) % findVal
                storeCmds_hand += shelfSave
                print storeCmds_hand

        #prompt dialog for artist to enter a name of the pose and button to save to shelf
        pd_hand = pm.promptDialog(t = "Hand Pose", m = "Name of Pose?", b = "Save to Shelf")


        if pd_hand == "Save to Shelf":

            pd_hand_name = pm.promptDialog(q = True, text = True)
            #pm.internalVar(usd = True)
            pm.shelfButton(l = pd_hand_name, ann = pd_hand_name, imageOverlayLabel = pd_hand_name, i1 = "zenRemember_handIcon.png", command = storeCmds_hand, p = target_handShelf, sourceType = "mel")



def saveToTab_leg(target_legShelf):
    #Clear out old data to store clean new data
    storeCmds_leg = ""

    #List selected
    selPose = pm.ls(sl = True)

    #Error window if nothing selected
    #List keyable, readable, writable, connectable, and unlocked attributes in selected
    #Grab values of selected and concatenates keyable channels
    if len(selPose) < 1:
        pm.warning("Nothing Selected.  Please select at least one object.")
    else:
        for all in selPose:
            keyable = pm.listAttr(all, k = True, r = True, w = True, c = True, u = True)
            print keyable
            for vals in keyable:
                findVal = pm.getAttr(all + "." + vals)
                print findVal
                starterCiph = "setAttr "
                enderCiph = ";\n"
                shelfSave = (starterCiph + (all + "." + vals) + " %f" + enderCiph) % findVal
                storeCmds_leg += shelfSave
                print storeCmds_leg

        #prompt dialog for artist to enter a name of the pose and button to save to shelf
        pd_leg = pm.promptDialog(t = "Leg Pose", m = "Name of Pose?", b = "Save to Shelf")


        if pd_leg == "Save to Shelf":

            pd_leg_name = pm.promptDialog(q = True, text = True)
            #pm.internalVar(usd = True)
            pm.shelfButton(l = pd_leg_name, ann = pd_leg_name, imageOverlayLabel = pd_leg_name, i1 = "zenRemember_legsIcon.png", command = storeCmds_leg, p = target_legShelf, sourceType = "mel")



def saveToTab_feet(target_feetShelf):
    #Clear out old data to store clean new data
    storeCmds_feet = ""

    #List selected
    selPose = pm.ls(sl = True)

    #Error window if nothing selected
    #List keyable, readable, writable, connectable, and unlocked attributes in selected
    #Grab values of selected and concatenates keyable channels
    if len(selPose) < 1:
        pm.warning("Nothing Selected.  Please select at least one object.")
    else:
        for all in selPose:
            keyable = pm.listAttr(all, k = True, r = True, w = True, c = True, u = True)
            print keyable
            for vals in keyable:
                findVal = pm.getAttr(all + "." + vals)
                print findVal
                starterCiph = "setAttr "
                enderCiph = ";\n"
                shelfSave = (starterCiph + (all + "." + vals) + " %f" + enderCiph) % findVal
                storeCmds_feet += shelfSave
                print storeCmds_feet

        #prompt dialog for artist to enter a name of the pose and button to save to shelf
        pd_feet = pm.promptDialog(t = "Feet Pose", m = "Name of Pose?", b = "Save to Shelf")


        if pd_feet == "Save to Shelf":

            pd_feet_name = pm.promptDialog(q = True, text = True)
            #pm.internalVar(usd = True)
            pm.shelfButton(l = pd_feet_name, ann = pd_feet_name, imageOverlayLabel = pd_feet_name, i1 = "zenRemember_feetIcon.png", command = storeCmds_feet, p = target_feetShelf, sourceType = "mel")
