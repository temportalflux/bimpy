import bimpy

ctx = bimpy.Context()

ctx.init(600, 600, "Bimpy Docking")

str = bimpy.String()
f = bimpy.Float();
main_dockspace_isopen = bimpy.Bool()

def create_main_dockspace():
	bimpy.set_next_window_pos(bimpy.get_viewport_pos())
	bimpy.set_next_window_size(bimpy.get_viewport_size())
	bimpy.push_style_var(bimpy.Style.WindowRounding, 0)
	bimpy.push_style_var(bimpy.Style.WindowBorderSize, 0)
	bimpy.push_style_var(bimpy.Style.FrameBorderSize, 0)
	bimpy.begin("Main", main_dockspace_isopen,
		bimpy.WindowFlags.MenuBar
		| bimpy.WindowFlags.NoDocking
		| bimpy.WindowFlags.NoTitleBar
		| bimpy.WindowFlags.NoCollapse
		| bimpy.WindowFlags.NoResize
		| bimpy.WindowFlags.NoMove
		| bimpy.WindowFlags.NoBringToFrontOnFocus
		| bimpy.WindowFlags.NoNavFocus
	)
	bimpy.pop_style_var(3)
	bimpy.DockSpace("DockSpace")
	bimpy.end()

while(not ctx.should_close()):
	ctx.new_frame()
	create_main_dockspace()
	if bimpy.begin("Window 1"):
		bimpy.text("Test window 1")
		bimpy.end()
	ctx.render()
