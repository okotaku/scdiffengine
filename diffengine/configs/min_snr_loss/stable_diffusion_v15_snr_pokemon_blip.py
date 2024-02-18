from mmengine.config import read_base

with read_base():
    from .._base_.datasets.pokemon_blip import *
    from .._base_.default_runtime import *
    from .._base_.models.stable_cascade import *
    from .._base_.schedules.stable_diffusion_50e import *


model.update(loss=dict(type="SNRL2Loss", snr_gamma=5.0, loss_weight=1.0))
