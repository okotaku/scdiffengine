from diffusers import AutoencoderKL, DDPMScheduler, UNet2DConditionModel
from transformers import CLIPTextModel, CLIPTokenizer

from diffengine.models.editors import StableCascade
from diffengine.models.editors.stable_cascade.data_preprocessor import (
   SDDataPreprocessor,
)
from diffengine.models.losses import L2Loss

base_model = "diffusers/tiny-stable-diffusion-torch"
model = dict(
            type=StableCascade,
             model=base_model,
             tokenizer=dict(type=CLIPTokenizer.from_pretrained,
                            subfolder="tokenizer"),
             scheduler=dict(type=DDPMScheduler.from_pretrained,
                            subfolder="scheduler"),
             text_encoder=dict(type=CLIPTextModel.from_pretrained,
                               subfolder="text_encoder"),
             vae=dict(
                type=AutoencoderKL.from_pretrained,
                subfolder="vae"),
             unet=dict(type=UNet2DConditionModel.from_pretrained,
                             subfolder="unet"),
            data_preprocessor=dict(type=SDDataPreprocessor),
            loss=dict(type=L2Loss))
