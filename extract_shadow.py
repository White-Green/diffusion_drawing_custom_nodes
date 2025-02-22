import torch


class ExtractShadow:
    UNIQUE_NAME = "DiffusionDrawingExtractShadow"
    DISPLAY_NAME = "Extract Shadow"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {"base_colored": ("IMAGE", {}), "shadow_applied": ("IMAGE", {}), "color_mask": ("MASK", {})},
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image_out",)
    CATEGORY = "diffusion drawing"
    FUNCTION = "extract_shadow"

    def extract_shadow(self, base_colored: torch.Tensor, shadow_applied: torch.Tensor, color_mask: torch.Tensor) -> (torch.Tensor,):
        # base_colored: [B, H, W, 3]
        # shadow_applied: [B, H, W, 3]
        # color_mask: [B, H, W]
        mask = torch.logical_and((base_colored > shadow_applied).all(dim=3), color_mask < 1)
        ratio = shadow_applied / base_colored
        ratio[torch.stack([torch.all(ratio > 0.95, dim=3)] * 3, dim=3)] = 1
        alpha = 1 - torch.mean(ratio, dim=3)
        alpha[(alpha < 0.1) | mask.logical_not() | alpha.isnan()] = 0

        return (torch.cat([torch.zeros_like(base_colored), alpha.unsqueeze(-1)], dim=3),)
