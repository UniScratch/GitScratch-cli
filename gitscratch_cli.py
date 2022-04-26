import zipfile, os, sys
import click, requests

@click.command()
def cli():
    """GitScratch 的命令行接口。"""
    click.echo("""GitScratch 的命令行接口。
v0.1

要查看更多信息，请运行 """ + os.path.abspath(sys.argv[0]) + " --help。")

# @click.command()
# def init():
#     """初始化一个空作品"""
#     with zipfile.ZipFile(
#         os.path.join(
#             os.getcwd(),
#             os.path.basename(os.getcwd())
#         ),
#         "x",
#         encoding="utf-8"
#     ) as new_project:
#         new_project.write("project.json")
#         new_project.write("b3c14cc491d535cc46c05df8bf389cb5.svg")
#         with new_project.open("projects.json", "w", encoding="utf-8") as project_obj:
#             project_obj.write('{"targets":[{"isStage":true,"name":"Stage","variables":{},"lists":{},"broadcasts":{},"blocks":{},"comments":{},"currentCostume":0,"costumes":[{"assetId":"b3c14cc491d535cc46c05df8bf389cb5","name":"背景1","md5ext":"b3c14cc491d535cc46c05df8bf389cb5.svg","dataFormat":"svg","rotationCenterX":240,"rotationCenterY":180}],"sounds":[],"volume":100,"layerOrder":0,"tempo":60,"videoTransparency":50,"videoState":"on","textToSpeechLanguage":null}],"monitors":[],"extensions":[],"meta":{"semver":"3.0.0","vm":"0.2.0-prerelease.20220222132735","agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Scratch/3.29.1 Chrome/94.0.4606.81 Electron/15.3.1 Safari/537.36"}}')
#         with new_project.open("b3c14cc491d535cc46c05df8bf389cb5.svg", "w", encoding="utf-8") as f_obj:
#             f_obj.write('<svg version="1.1" viewBox="-1 -1 2 2" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"></svg>')

if __name__ == "__main__":
    cli()