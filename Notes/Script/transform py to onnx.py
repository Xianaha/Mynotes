import torch
import torch.onnx
from torch.nn import CNN

def transform_pth_to_onnx(model_class, img_size, model_path):
    model = model_class()
    model.load_state_dict(torch.load(model_path))
    model.eval()
    onnx_path = os.path.splitext(model_path)[0] + ".onnx"
    
    input = torch.randn(1, 3, img_size, img_size)
    torch.onnx.export(model,
                      input,
                      onnx_path,
                      export_params=True,
                      opset_version=11,
                      do_constant_folding=True
        
    )

transform_pth_to_onnx(CNN, 224,"/data/wang_xian/IdentifyCats,dogs,andfoxes/MyResNet_model.pt")
