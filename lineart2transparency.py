import torch

class Lineart2Transparency:
    UNIQUE_NAME = "DiffusionDrawingLineart2Transparency"
    DISPLAY_NAME = "Lineart to Transparency"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": { "image_in" : ("IMAGE", {}) },
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image_out",)
    CATEGORY = "diffusion drawing"
    FUNCTION = "lineart2transparency"

    def lineart2transparency(self, image_in: torch.Tensor) -> (torch.Tensor, ):
        zero = torch.zeros((*image_in.shape[0:3], 3), dtype=image_in.dtype)
        transparency = 1 - image_in[:, :, :, 0:1]
        transparency[transparency < 0.1] = 0
        image_out = torch.cat([zero, transparency], dim=3)
        return (image_out,)
