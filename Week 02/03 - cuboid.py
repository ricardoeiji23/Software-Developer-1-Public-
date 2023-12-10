width = int(input("Write the value of the cuboid's width: ")) #Largura
length = int ((input("Write the value of the cuboid's length: "))) #Comprimento
height = int (input("Write the value of the cuboid's height: ")) #Altura

cuboid_surface_area = (2*(length*width + width*height + length*height))
    # The surface area is -> Surface Area=2lw+2lh+2wh
        # l=length (Comprimento)
        # w=width (Largura)
        # h=height (Altura)

cuboid_volume = (width*length*height)
    #Area of cuboid (l*w*h)

print("\nThe surface area is:",str(cuboid_surface_area))

print("The volume of the cuboid is:", str(cuboid_volume))
