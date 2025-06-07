
from docx import Document

def load_docx(docx_file):
    doc = Document(docx_file)
    return "\n".join([p.text for p in doc.paragraphs if p.text.strip() != ""])

def annotate_text(text):
    # Placeholder logic for annotation and edits
    clean_version = text.replace("violence", "aggressive behavior")
    annotated_version = text + "\n\n[NOTE: Consider citing REBT theory here.]"
    return clean_version, annotated_version

def generate_bibliography():
    return (
        "Ellis, A., & Dryden, W. (1997). *The Practice of Rational Emotive Behavior Therapy*. Springer.\n"
        "Johnson, M. P. (2006). Conflict and control: Gender symmetry and asymmetry in domestic violence. *Violence Against Women, 12*(11), 1003–1018.\n"
        "Straus, M. A., Gelles, R. J., & Steinmetz, S. K. (1980). *Behind Closed Doors: Violence in the American Family*. Anchor Books."
    )
