import torch


class FakeShadow:
    UNIQUE_NAME = "DiffusionDrawingFakeShadow"
    DISPLAY_NAME = "Fake Shadow"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {"base_image": ("IMAGE", {}), "color_mask": ("MASK", {})},
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image_out",)
    CATEGORY = "diffusion drawing"
    FUNCTION = "fake_shadow"

    def fake_shadow(self, base_image: torch.Tensor, color_mask: torch.Tensor) -> (torch.Tensor,):
        # base_image: [B, H, W, 3]
        # color_mask: [B, H, W]
        shadow = torch.sqrt(torch.rand_like(color_mask))
        shadow[torch.logical_or(color_mask > 0, shadow < 0.9)] = 1

        return (base_image * torch.stack([shadow] * 3, dim=3),)
