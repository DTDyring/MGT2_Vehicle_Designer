

# Mongoose Traveller 2 Vehicle Designer

## PROGRAM NEEDS:
  - GUI! GUI! GUI!
      - Organically add/remove customizations
      - Organically add/remove weapon mounts
      - Organically add/remove weapons to weapon mounts
         - Organically add/remove different loadouts for vehicle?
      - Collapse/expand sections
         - Collapse/expand individual members of sections?
      - Multiple methods for add/remove to a vehicle
         - Drag and Drop
         - Add/Remove button
  - Contain all types of vehicles
  - Contain all types of traits
  - Contain all types of quirks
  - A report of the vehicle w/ all important info
     - Updates as changes are made
     - Can be sent to clipboard instantly(?)
     - Can be saved as a vehicle report
  - Save the current vehicle being worked on
     - Can load immediately
     - Loads most recent vehicle when app is launched

## WHAT MAKES A VEHICLE:
  - Tech Level
     - 1-15
     - Determines many basic stats
     - Controls component availability
  - Chassis
     - Multiple types (light/heavy ground, ship, grav, etc.)
     - Minimum/maximum Space amounts
     - Hull/Space
     - Different Chassis customizations for different chassis
     - Different Skills for different chassis
     - Spaces/personnel (maybe its own heading?)
  - Armor
     - Multiple types
     - Custom facings (need to understand how rules manage this)
     - Minimum starting Armor for vehicles per armor type & tech level
     - Consumes Spaces
  - Armaments
     - Several mounting types (turrets, fixed, pintle, hardpoint, etc.)
        - Weapon facing
        - Some have a maximum total spaces they can occupy on a vehicle (e.g. hardpoints <= 25% of Chassis Spaces)
     - Mount customizations
     - Several weapon types
     - Spaces management
        - Chassis Space usage
        - Mount Space usage
     - Spacecraft weapons
     - Weapon modifications
  - Customizations
     - Multiple types
     - Drones (control systems?)
     - Robots (control systems?)

## Notes
[1] if a vehicle is a Rail Rider, need a checkbox to appear for if capable of off-rail travel
[2] if a vehicle is a Sub and uses the Increased Dive customization, there needs to be a special set of UI elements to
    allow increasing Cost per Space (by increments of 1%) and the effect that would have on its Armor, Safe Depth, and
    Crush Depth.