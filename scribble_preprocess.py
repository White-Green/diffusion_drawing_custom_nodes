import sys
import torch


class ScribblePreprocess:
    UNIQUE_NAME = "DiffusionDrawingScribblePreprocess"
    DISPLAY_NAME = "Scribble Preprocess"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {"image_in": ("IMAGE", {})},
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image_out",)
    CATEGORY = "diffusion drawing"
    FUNCTION = "scribble_preprocess"

    def scribble_preprocess(self, image_in: torch.Tensor) -> (torch.Tensor,):
        m = torch.min(torch.min(image_in[:, :, :, 0], image_in[:, :, :, 1]), image_in[:, :, :, 2])
        one_channel = 1 - m
        image_out = torch.stack([one_channel] * 3, dim=3)
        return (image_out,)
