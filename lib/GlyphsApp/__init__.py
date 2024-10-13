from GlyphsApp.GSFont import GSFont
from GlyphsApp.GSApplication import GSApplication
from GlyphsApp.GSLayer import GSLayer


Glyphs = GSApplication()
Glyphs.font = GSFont()

__all__ = ["GSFont", "GSApplication", "GSLayer", "Glyphs"]
