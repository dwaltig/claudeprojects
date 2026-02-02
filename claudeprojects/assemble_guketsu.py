import os

base_path = "Miao-lo/Guketsu_Project/01_TRANSLATIONS"
versions = ["Scholarly", "Blues"]

def assemble_version(version):
    output_filename = f"Guketsu_Complete_{version}.md"
    output_path = os.path.join(base_path, output_filename)
    
    print(f"Assembling {version} version into {output_path}...")
    
    with open(output_path, "w", encoding="utf-8") as outfile:
        # Title Page
        title = "Miao-lo's Guketsu (Hongjue) - Complete Translation"
        subtitle = "Scholarly Edition" if version == "Scholarly" else "The Blues Interpretation"
        outfile.write(f"# {title}\n")
        outfile.write(f"## {subtitle}\n\n")
        outfile.write("---\n\n")

        for i in range(1, 11): # Fascicles 1 to 10
            fascicle_num = f"{i:02d}"
            print(f"  Processing Fascicle {fascicle_num}...")
            
            # 1. Opening
            opening_file = os.path.join(base_path, f"Fascicle_{fascicle_num}_Opening_{version}.md")
            if os.path.exists(opening_file):
                outfile.write(f"\n\n<!-- FASCICLE {fascicle_num} OPENING -->\n\n")
                with open(opening_file, "r", encoding="utf-8") as infile:
                    outfile.write(infile.read())
                    outfile.write("\n\n---\n\n")
            
            # 2. Preface (Only Fascicle 1 usually, but generic check is safe)
            preface_file = os.path.join(base_path, f"Fascicle_{fascicle_num}_Preface_{version}.md")
            if os.path.exists(preface_file):
                outfile.write(f"\n\n<!-- FASCICLE {fascicle_num} PREFACE -->\n\n")
                with open(preface_file, "r", encoding="utf-8") as infile:
                    outfile.write(infile.read())
                    outfile.write("\n\n---\n\n")

            # 3. Sections
            for j in range(1, 20): # Assuming max 20 sections per fascicle
                section_num = f"{j:02d}"
                # Try different naming conventions if necessary, but standard seems to be Section_XX
                section_file = os.path.join(base_path, f"Fascicle_{fascicle_num}_Section_{section_num}_{version}.md")
                
                # Handling slight naming variation if any (e.g. Section02 vs Section_02)
                if not os.path.exists(section_file):
                     section_file_alt = os.path.join(base_path, f"Fascicle_{fascicle_num}_Section{section_num}_{version}.md")
                     if os.path.exists(section_file_alt):
                         section_file = section_file_alt
                
                if os.path.exists(section_file):
                    outfile.write(f"\n\n<!-- FASCICLE {fascicle_num} SECTION {section_num} -->\n\n")
                    with open(section_file, "r", encoding="utf-8") as infile:
                        outfile.write(infile.read())
                        outfile.write("\n\n---\n\n")

            # 4. Closing Summary
            closing_file = os.path.join(base_path, f"Fascicle_{fascicle_num}_Closing_Summary_{version}.md")
            if os.path.exists(closing_file):
                outfile.write(f"\n\n<!-- FASCICLE {fascicle_num} CLOSING -->\n\n")
                with open(closing_file, "r", encoding="utf-8") as infile:
                    outfile.write(infile.read())
                    outfile.write("\n\n---\n\n")
    
    print(f"Finished {version} version.")

for v in versions:
    assemble_version(v)
