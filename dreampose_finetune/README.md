1. Model Structure
   1. Paper: https://arxiv.org/pdf/2304.06025.pdf
   2. Sub-modules:
      1. CLIP encoder
      2. VAE encoder
      3. UNet: stable diffusion
      4. VAE Decoder
      5. Adapter (VAE embedding + MLP add CLIP embedding ==> Embedding for UNet)
2. Requirements
    accelerate==0.21.0
    diffusers==0.18.2
    einops==0.6.1
    huggingface-hub==0.16.4
    numpy==1.22.4
    tensorboard==2.9.1
    torch==1.11.0
    torchvision==0.12.0
    transformers==4.30.2
3. Finetune on Sample
   1. Finetune the Unet:
       accelerate launch main_finetune_unet.py --pretrained_model_name_or_path="CompVis/stable-diffusion-v1-4" --instance_data_dir=demo/sample/train --output_dir=demo/custom-chkpts --resolution=512 --train_batch_size=1 --gradient_accumulation_steps=1 --learning_rate=1e-5 --num_train_epochs=500 --dropout_rate=0.0 --custom_chkpt=demo/custom-chkpts/unet_epoch_499.pth --revision "ebb811dd71cdc38a204ecbdd6ac5d580f529fd8c"  
   2. Finetune the VAE:
       accelerate launch --num_processes=1 finetune-vae.py --pretrained_model_name_or_path="CompVis/stable-diffusion-v1-4"  --instance_data_dir=demo/sample/train --output_dir=demo/custom-chkpts --resolution=512  --train_batch_size=4 --gradient_accumulation_steps=4 --learning_rate=5e-5 --num_train_epochs=1500 --custom_chkpt=demo/custom-chkpts/unet_epoch_499.pth --run_name finetuning/ubc-vae --revision "ebb811dd71cdc38a204ecbdd6ac5d580f529fd8c"
4. Testing
      1. Download and unzip the pretrained models inside demo/custom-chkpts.zip
      2. Download and unzip the input poses inside demo/sample/poses.zip
      3. Run test.py using the command below:
          python test.py --epoch 499 --folder demo/custom-chkpts --pose_folder demo/sample/poses  --key_frame_path demo/sample/key_frame.png --s1 8 --s2 3 --n_steps 100 --output_dir demo/sample/results --custom_vae demo/custom-chkpts/vae_1499.pth

   