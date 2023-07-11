1. Model Structure
   1. Paper: https://arxiv.org/pdf/2304.06025.pdf
   2. Sub-modules:
      1. CLIP encoder
      2. VAE encoder
      3. UNet: stable diffusion
      4. VAE Decoder
      5. Adapter (VAE embedding + MLP add CLIP embedding ==> Embedding for UNet)
2. 