from .lineart2transparency import Lineart2Transparency
from .scribble_preprocess import ScribblePreprocess
from .extract_shadow import ExtractShadow
from .extract_light import ExtractLight
from .fake_shadow import FakeShadow

NODE_CLASS_MAPPINGS = {
    Lineart2Transparency.UNIQUE_NAME: Lineart2Transparency,
    ScribblePreprocess.UNIQUE_NAME: ScribblePreprocess,
    ExtractShadow.UNIQUE_NAME: ExtractShadow,
    ExtractLight.UNIQUE_NAME: ExtractLight,
    FakeShadow.UNIQUE_NAME: FakeShadow,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    Lineart2Transparency.UNIQUE_NAME: Lineart2Transparency.DISPLAY_NAME,
    ScribblePreprocess.UNIQUE_NAME: ScribblePreprocess.DISPLAY_NAME,
    ExtractShadow.UNIQUE_NAME: ExtractShadow.DISPLAY_NAME,
    ExtractLight.UNIQUE_NAME: ExtractLight.DISPLAY_NAME,
    FakeShadow.UNIQUE_NAME: FakeShadow.DISPLAY_NAME,
}
