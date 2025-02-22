import torch


class ExtractLight:
    UNIQUE_NAME = "DiffusionDrawingExtractLight"
    DISPLAY_NAME = "Extract Light"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {"base_colored": ("IMAGE", {}), "light_applied": ("IMAGE", {}), "color_mask": ("MASK", {})},
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image_out",)
    CATEGORY = "diffusion drawing"
    FUNCTION = "extract_light"

    def extract_light(self, base_colored: torch.Tensor, light_applied: torch.Tensor, color_mask: torch.Tensor) -> (torch.Tensor,):
        # base_colored: [B, H, W, 3]
        # shadow_applied: [B, H, W, 3]
        # color_mask: [B, H, W]
        mask = torch.logical_and((base_colored < light_applied).all(dim=3), color_mask < 1)
        ratio = (light_applied - base_colored) * torch.stack([mask] * 3, dim=3)
        alpha = torch.mean(ratio, dim=3)
        alpha[alpha < 0.1] = 0

        return (torch.cat([torch.ones_like(base_colored), alpha.unsqueeze(-1)], dim=3),)
