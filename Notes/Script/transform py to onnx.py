import torch
import torch.onnx
from torch.nn import CNN

def transform_pth_to_onnx(model_class, dummy_input, model_path, onnx_path):
    model = model_class()
    model.load_state_dict(torch.load(model_path))
    model.eval()
    
    input = dummy_input
    torch.onnx.export(model,
                      dummy_input,
                      onnx_path,
                      export_params=True,
                      opset_version=11,
                      do_constant_folding=True
        
    )

transform_pth_to_onnx(model_class=CNN, dummy_input=torch.randn(1, 3, 128, 128), model_path='/data/wang_xian/IdentifyCats,dogs,andfoxes/model.pth', onnx_path='/data/wang_xian/IdentifyCats,dogs,andfoxes/model.onnx')
