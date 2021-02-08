
def initialise():

  print("##########################")
  print("## FOCUS ICON GENERATOR ##")
  print("##########################")

  try:
    goals = open("goals.gfx", "x")
    goals_write = open("goals.gfx", "a")
  except:
    goals_clear = open("goals.gfx", "w")
    goals_clear.write("")
    goals_clear.close()
    goals_write = open("goals.gfx", "a")

  try:
    goals_shine = open("goals_shine.gfx", "x")
    goals_shine_write = open("goals_shine.gfx", "a")
  except:
    goals_shine_clear = open("goals_shine.gfx", "w")  
    goals_shine_clear.write("")
    goals_shine_clear.close()
    goals_shine_write = open("goals_shine.gfx", "a")

  goals_write.write("SpriteTypes = {\n")
  goals_write.close()

  goals_shine_write.write("SpriteTypes = {\n")
  goals_shine_write.close()

  while True:

    focus_name = input("Focus name: ")

    if focus_name == "Done":
      
      f = open("goals.gfx", "a")
      f.write("\n}")
      f.close()

      f = open("goals_shine.gfx", "a")
      f.write("\n}")
      f.close()

      return False

    f = open("goals.gfx", "a")

    string = "\n    SpriteType = {\n        name = \"GFX_focus_" + focus_name + "_shine\"\n        texturefile = \"gfx/interface/goals/" + focus_name + ".dds\"\n    }\n" 
    f.write(string)
    f.close()

    f = open("goals_shine.gfx", "a")

    string = "\n    SpriteType = {\n        name = \"GFX_focus_" + focus_name + "_shine\"\n        texturefile = \"gfx/interface/goals/" + focus_name + ".dds\"\n        effectFile = \"gfx/FX/buttonstate.lua\"\n\n        animation = {\n            animationmaskfile = \"gfx/interface/goals/" + focus_name + ".dds\"\n            animationtexturefile = \"gfx/interface/goals/shine_overlay.dds\"\n            animationrotation = -90.0\n            animationlooping = no\n            animationtime = 0.75\n            animationdelay = 0\n            animationblendmode = \"add\"\n            animationtype = \"scrolling\"\n            animationrotationoffset = { x = 0.0 y = 0.0 }\n            animationtexturescale = { x = 1.0 y = 1.0 }\n        }\n\n        animation = {\n            animationmaskfile = \"gfx/interface/goals/" + focus_name + ".dds\"\n            animationtexturefile = \"gfx/interface/goals/shine_overlay.dds\"\n            animationrotation = 90.0\n            animationlooping = no\n            animationtime = 0.75\n            animationdelay = 0\n            animationblendmode = \"add\"\n            animationtype = \"scrolling\"\n            animationrotationoffset = { x = 0.0 y = 0.0 }\n            animationtexturescale = { x = 1.0 y = 1.0 }\n        }\n\n	legacy_lazy_load = no    }\n" 
    f.write(string)
    f.close()

    #print("\033[1;32;40mDone.\033[0m")

initialise()