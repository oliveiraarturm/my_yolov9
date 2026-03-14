import argparse

def parse_opt(known=False):
    parser = argparse.ArgumentParser()
    parser.add_argument('--hyp', type=str, help='hyperparameters path')
    return parser.parse_known_args()[0] if known else parser.parse_args()

if __name__ == "__main__":
    opt = parse_opt()