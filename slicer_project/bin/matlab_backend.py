import matlab.engine

def run_matlab_slicer(input_stl, output_gcode, layer_height, shell_thickness, infill_density, print_speed):
    '''
    Interface for calling MATLAB backend slicer. 
    '''
    eng = matlab.engine.start_matlab()

    try:
        # Create MATLAB expected inputs as a string
        matlab_command = f"""
        filname = '{input_stl}';
        gfilename = '{output_gcode}';
        layer_hight = {layer_height};
        shell_thick = {shell_thickness};
        infill_density = {infill_density};
        print_speed = {print_speed};
        main;
        """

        print("------ MATLAB command ------")
        print(matlab_command)

        # Execute the MATLAB command block
        eng.eval(matlab_command, nargout=0)
    
    except matlab.engine.MatlabExecutionError as e:
        print("MATLAB runtime error:", e)

    finally:
        # Close MATLAB engine, regardless of errors
        eng.quit()

    # ----- Original implementation for reference -----
    # MATLAB integration required MATLAB and MATLAB Engine 
    # eng.eval(f"filenam = '{input_stl}';", nargout=0)
    # eng.eval(f"gfilename = '{output_gcode}';", nargout=0)
    # eng.eval(f"layer_hight = {layer_height};", nargout=0)
    # eng.eval(f"shell_thick = {shell_thickness};", nargout=0)
    # eng.eval(f"infill_density = {infill_density};", nargout=0)
    # eng.eval(f"print_speed = {print_speed};", nargout=0)
    # eng.eval("main;", nargout=0)
    # eng.quit()

