Translucent/Transparent design:
1) Investigate a customised blender, using graphics, pick a comfortable/good renderer
2) Investigate what it would take to transfer one of those meshes into NOME/JIPCAD
3) Maybe using STL files? That can help with the rendering, since all the files can be customised. 

Take neat cool gemoetry in the format of STL file
- Input format, a little translater, essentially called STL to jipcad. For every triangle it finds in the STL, it creates triangle in jipcad. 
- Ideally it would be cool to make a translater to convert stl files directly to nome. 
- Do the triangles, translate the

STL will first create triangles:
- Breaks into triangles

Export STL without merging.

STL breaks up the points of the shape into triangles in an intelligent way. 

Non-planar facces -> It really kind of matters how you split them into triangles(depending on the diagonals)

If you do a sweep -> with no twist -> then whatever
But if there is a twist -> Then the nome thing needs to have a good triangle. 

It would be bad if you have non-planar quadrilaterals and then you would want the non-planar body into planar quads. 

Non-planar quadrilaterals, just break it into planar triangles.

That is kinda what STL files does. 
