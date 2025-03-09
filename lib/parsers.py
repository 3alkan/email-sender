from lib.logger import logger

def parse_recipients(content:str):
    """
    * Structure of this function can be change from project to project
    Reads recipients from a file.
    Format: email,name (if no name, defaults to "Yetkili").
    Returns a list of dictionaries with 'email' and 'name' keys.
    """
    recipients = []
    try:
        content=content.split("\n")
        for line in content:
            if not line.strip():
                continue
            parts = line.strip().split(",")  # Expected format: email,name
            if len(parts) == 2:
                recipients.append({"email": parts[0].strip(), "name": parts[1].strip()})
            else:
                recipients.append({"email": parts[0].strip(), "name": "Yetkili"})
    except Exception as e:
        logger.error(f"Error in parse_recipients: ",e)
    return recipients
