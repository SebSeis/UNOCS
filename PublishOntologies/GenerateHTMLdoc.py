from pylode import MakeDocco
from os.path import join, dirname, abspath
from pathlib import Path

def generate_documentation():
    # Get the directory where the script is located
    script_dir = dirname(abspath(__file__))
    
    # Define the input ontology file and the output HTML file
    ontology_file = join(script_dir, "20241212UNOCSpublic.ttl")
    output_file = join(script_dir, "20241212UNOCSpublic.html")
    
    # Convert the ontology file path to a file URI
    ontology_uri = Path(ontology_file).absolute().as_uri()
    
    # Print paths for verification
    print(f"Ontology file URI: {ontology_uri}")
    print(f"Output HTML path: {output_file}")
    
    # Initialize the MakeDocco class with the ontology URI and desired output format
    doc_generator = MakeDocco(input_data_file=ontology_uri, outputformat="html")
    
    # Generate the HTML documentation
    doc_generator.document(destination=output_file)
    
    print(f"Documentation successfully generated at: {output_file}")

if __name__ == "__main__":
    generate_documentation()
